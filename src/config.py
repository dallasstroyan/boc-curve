from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = PROJECT_ROOT / "data" / "raw"
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
OUTPUT_DIR = PROJECT_ROOT / "output"

for d in (RAW_DIR, PROCESSED_DIR, OUTPUT_DIR):
    d.mkdir(parents=True, exist_ok=True)

DEFAULT_START_DATE = "2015-01-01"
COMPOUNDING_FREQ = 2          # semi-annual, GoC convention
DAY_COUNT = "ACT/365"
CACHE_MAX_AGE_HOURS = 24

SERIES_SETS = {
    "goc_benchmarks": { # Years
        "BD.CDN.2YR.DQ.YLD": 2.0,
        "BD.CDN.3YR.DQ.YLD": 3.0,
        "BD.CDN.5YR.DQ.YLD": 5.0,
        "BD.CDN.7YR.DQ.YLD": 7.0,
        "BD.CDN.10YR.DQ.YLD": 10.0,
        "BD.CDN.LONG.DQ.YLD": 30.0,   # nominal; actual maturity drifts
    },
    "goc_tbills": { # Year fractions
        "TB.CDN.30D.MID": 30/365,
        "TB.CDN.60D.MID": 60/365,
        "TB.CDN.90D.MID": 90/365,
        "TB.CDN.180D.MID": 180/365,
        "TB.CDN.1Y.MID": 1.0,
    }
}



