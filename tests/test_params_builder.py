import pytest

from silentpush.params_builder import build_infratag_params

"""Parameter builder tests"""


def test_build_infratag_params_with_empty_params():
    assert build_infratag_params("", "", "") == {}


def test_build_infratag_params_with_mode():
    assert build_infratag_params("live", "", "") == {"mode": "live"}


def test_build_infratag_params_with_invalid_mode():
    with pytest.raises(ValueError, match=r"Mode must be either live or padns."):
        build_infratag_params("invalid mode", "", "")


def test_build_infratag_params_with_match():
    assert build_infratag_params("", "self", "") == {"match": "self"}


def test_build_infratag_params_with_invalid_match():
    with pytest.raises(ValueError, match=r"Match must be either self or full."):
        build_infratag_params("", "invalid match", "")


def test_build_infratag_params_with_as_of():
    assert build_infratag_params("padns", "", "2021-07-09") == {"mode": "padns", "as_of": "2021-07-09"}


def test_build_infratag_params_with_invalid_as_of():
    with pytest.raises(ValueError, match=r"as_of must be in iso date format, YYYY-MM-DD."):
        build_infratag_params("padns", "", "invalid date")


def test_build_infratag_params_with_as_of_and_wrong_mode():
    with pytest.raises(ValueError, match=r"When passing as_of, mode must be padns."):
        build_infratag_params("live", "", 20)
