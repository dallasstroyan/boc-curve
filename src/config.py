from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = PROJECT_ROOT / "data" / "raw"
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
OUTPUT_DIR = PROJECT_ROOT / "output"

DEFAULT_START_DATE = "2015-01-01"
COMPOUNDING_FREQ = 2          # semi-annual, GoC convention
DAY_COUNT = "ACT/365"
CACHE_MAX_AGE_HOURS = 24

GOC_BENCHMARKS = {
    "BD.CDN.2YR.DQ.YLD": 2,
    "BD.CDN.3YR.DQ.YLD": 3,
    "BD.CDN.5YR.DQ.YLD": 5,
    "BD.CDN.7YR.DQ.YLD": 7,
    "BD.CDN.10YR.DQ.YLD": 10,
    "BD.CDN.LONG.DQ.YLD": 30,   # nominal; actual maturity drifts
}

GOC_TBILLS = {
    "TB.CDN.30D.MID": 30,
    "TB.CDN.60D.MID": 60,
    "TB.CDN.90D.MID": 90,
    "TB.CDN.180D.MID": 180,
    "TB.CDN.1Y.MID": 1,
}