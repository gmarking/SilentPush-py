import silentpush.validators as validators

"""Helpful functions to build Silent Push API request parameters."""


def build_infratag_params(mode: str, match: str, as_of: str | int) -> dict[str, str | int]:
    """Returns valid infratag request parameters the caller provided.

    :param mode: <live|padns> build infratags from live lookup data or from PADNS data
    :param match: <self|full> handling of self-hosted infrastructure.
    :param as_of: build infratags from padns data where the as_of timestamp
        equivalent is between the first_seen and the last_seen timestamp

    :type mode: str
    :type match: str
    :type as_of: str | int

    :returns: dictionary of parameter key value pairs to be passed in request. 
    """
    params = {}
    if mode:
        validators.validate_mode(mode)
        params["mode"] = mode
    if match:
        validators.validate_match(match)
        params["match"] = match
    if as_of:
        validators.validate_as_of(as_of, mode)
        params["as_of"] = as_of
    return params
