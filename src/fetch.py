"""
TODO
Implement FRED request - DO LATER, GET GOC WORKING FIRST
Validation helper - To be added once FRED requests implemented
"""

import requests
import datetime as dt
from pathlib import Path
from src.config import SERIES_SETS, DEFAULT_START_DATE, RAW_DIR

def fetch_series(series_codes: list[str], start_date: str, label: str) -> Path:
    """GET from Valet, write raw JSON to data/raw/ with a UTC timestamp, 
    return the path written. Raises RuntimeError on request failure, malformed JSON, empty response, or missing series. Does not parse."""

    # Join the iterable and build the request URL for GOC Valet Requests
    codes_str = ",".join(series_codes)
    url = f"https://www.bankofcanada.ca/valet/observations/{codes_str}/json?start_date={start_date}"

    # request with timeout
    r = requests.get(url, timeout=30)

    # Error Handling
    if not r.ok:
        raise RuntimeError(f"Valet request failed ({r.status_code}) for {series_codes}: {r.text[:200]}")
    
    # Not JSON
    try:
        data = r.json()

    except ValueError as e:
        raise RuntimeError(f"Response was not valid JSON: {r.text[:200]}") from e

    # JSON but no observations
    if not data.get("observations"):
        raise RuntimeError(f"No observations returned for {series_codes} from {start_date}")

    # Check all series are present
    returned = set(data["observations"][0].keys()) - {"d"}
    missing = set(series_codes) - returned
    if missing:
        raise RuntimeError(f"Series missing from response: {missing}")
    
   # Get current time and format for filenaming
    current_time = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")

    # Set output path based on directories from config file, fetch label and current time
    out_path = RAW_DIR / f"{label}_{current_time}.json"

    out_path.write_text(r.text, encoding="utf-8")

    return out_path

if __name__ == "__main__":
    name = "GOC_BENCHMARKS"
    path = fetch_series(list(SERIES_SETS[name]), DEFAULT_START_DATE, label=name)
    print(f"Wrote {path}")