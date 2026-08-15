import requests
import json
from config import GOC_BENCHMARKS, GOC_TBILLS, DEFAULT_START_DATE

Path = vars

def fetch_series(series_codes: list[str], start_date: str) -> Path:
    """GET from Valet, write raw JSON to data/raw/ with a UTC timestamp, 
    return the path written. Raises on non-200. Does not parse."""
    url = f"https://www.bankofcanada.ca/valet/observations/{series_codes}/json?start_date={start_date}"

    r = requests.get(url)

    status = r.status_code

    print(status)
    print(start_date)
    
    print(r.json())
    return Path
   
series_codes = ",".join(GOC_BENCHMARKS | GOC_TBILLS)

Path = fetch_series(series_codes, DEFAULT_START_DATE)