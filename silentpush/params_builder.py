def build_infratag_params(mode: str, match: str, as_of: str | int) -> dict[str, str | int]: 
    params = {}
    if mode:
        params["mode"] = mode
    if match:
        params["match"] = match
    if as_of:
        params["as_of"] = as_of
    return params