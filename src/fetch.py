"""TODO
Status error messages
Implement FRED request
Seperate requests for Bonds and bills

"""

import requests
import json
import datetime as dt
from pathlib import Path
from src.config import GOC_BENCHMARKS, GOC_TBILLS, DEFAULT_START_DATE, RAW_DIR

def fetch_series(series_codes: list[str], start_date: str) -> Path:
    """GET from Valet, write raw JSON to data/raw/ with a UTC timestamp, 
    return the path written. Raises on non-200. Does not parse."""

    url = f"https://www.bankofcanada.ca/valet/observations/{series_codes}/json?start_date={start_date}"

    current_time = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")

    out_path = RAW_DIR / f"goc_{current_time}.json"

    r = requests.get(url, timeout=30)

    # Error Handling
    if not r.ok():
        raise RuntimeError(f"Valet request failed ({r.status_code}) for {series_codes}: {r.text[:200]}")

    try:
        data = r.json()
    except ValueError as e:
        raise RuntimeError(f"Response not was not valid JSON: {r.text[:200]}") from e

    if not data.get("observations"):
        raise RuntimeError(f"No observations returned for {series_codes} from {start_date}")

    #Check status
    status = r.status_code

    if status == 200:
        data = r.json()

        with open(out_path, "w", encoding = "utf-8") as f:
            json.dump(data, f, indent = 4)

        return out_path
        
    else: return None

series_codes = ",".join(GOC_BENCHMARKS | GOC_TBILLS)

written_path = fetch_series(series_codes, DEFAULT_START_DATE)

if __name__ == "__main__":
    codes = ",".join(GOC_BENCHMARKS | GOC_TBILLS)
    path = fetch_series(codes, DEFAULT_START_DATE)
    print(f"Wrote {path}")