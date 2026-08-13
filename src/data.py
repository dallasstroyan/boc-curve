# data.py
def load_goc_yields(force_refresh: bool = False) -> pd.DataFrame:
    """Return the tidy yield frame. Hits network only if cache is
    missing or stale."""