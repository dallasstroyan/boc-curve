"""
TODO
2 main functions:
1. Path plus mapping in, DataFrame out
2. Write frame to parquet

Data.py will decide when to call each
"""

import requests
import datetime as dt
from pathlib import Path
from src.config import SERIES_SETS, DEFAULT_START_DATE, RAW_DIR
from src.fetch import fetch_series

def parse_valet_json(path: Path, code_to_tenor: dict[str, int]) -> pd.DataFrame:
    """Read raw JSON, unwrap the nested {'v': ...} values, coerce to float,
    rename columns from series code to tenor, DatetimeIndex, sorted ascending."""