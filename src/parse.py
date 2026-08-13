def parse_valet_json(path: Path, code_to_tenor: dict[str, int]) -> pd.DataFrame:
    """Read raw JSON, unwrap the nested {'v': ...} values, coerce to float,
    rename columns from series code to tenor, DatetimeIndex, sorted ascending."""