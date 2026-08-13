def fetch_series(series_codes: list[str], start_date: str) -> Path:
    """GET from Valet, write raw JSON to data/raw/ with a UTC timestamp,
    return the path written. Raises on non-200. Does not parse."""
