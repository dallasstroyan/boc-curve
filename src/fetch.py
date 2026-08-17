"""TODO
Status error messages
"""

import requests
import json
import datetime as dt
from config import GOC_BENCHMARKS, GOC_TBILLS, DEFAULT_START_DATE, RAW_DIR

Path = vars

def fetch_series(series_codes: list[str], start_date: str) -> Path:
    """GET from Valet, write raw JSON to data/raw/ with a UTC timestamp, 
    return the path written. Raises on non-200. Does not parse."""

    url = f"https://www.bankofcanada.ca/valet/observations/{series_codes}/json?start_date={start_date}"

    current_time = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")

    r = requests.get(url)

    #Check status
    status = r.status_code

    if status == 200:
        data = r.json()

        with open(RAW_DIR/f"{current_time}.json", "w", encoding = "utf-8") as f:
            json.dump(data, f, indent = 4)

        return Path
        
    else: return None

series_codes = ",".join(GOC_BENCHMARKS | GOC_TBILLS)

Path = fetch_series(series_codes, DEFAULT_START_DATE)