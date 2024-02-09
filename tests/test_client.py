import httpretty
import pytest

from silentpush.client import Client

"""Client tests"""


def test_when_initializing_client_with_valid_api_key_then_no_exception_thrown():
    client = Client("dummy_api_key")
    assert client.headers == {"X-API-KEY": "dummy_api_key"}


def test_throws_value_error_when_initializing_given_bad_api_key():
    with pytest.raises(ValueError, match=r"API key must be a string."):
        Client(1)

    with pytest.raises(ValueError, match="API key must not be empty string."):
        Client("")


@httpretty.activate
def test_get_domain_with_valid_domain():
    httpretty.register_uri(
        httpretty.GET,
        "https://api.silentpush.com/api/v1/merge-api/explore/domain/domaininfo/dummy_domain.com",
        body='{"domain_info": "dummy_info"}',
    )
    client = Client("dummy_api_key")

    results = client.get_domain_information("dummy_domain.com")
    assert results == {"domain_info": "dummy_info"}


def test_get_domain_information_with_invalid_domain_raise_exception():
    client = Client("dummy_api_key")

    with pytest.raises(ValueError, match=r"Domain must be a string."):
        client.get_domain_information(1)


@httpretty.activate
def test_get_ip_information_with_valid_ip():
    httpretty.register_uri(
        httpretty.GET,
        "https://api.silentpush.com/api/v1/merge-api/explore/ipv4/ipv4info/1.1.1.1",
        body='{"ip_info": "dummy_info"}',
    )
    client = Client("dummy_api_key")

    results = client.get_ip_information("1.1.1.1")
    assert results == {"ip_info": "dummy_info"}

    results = client.get_ip_information("1.1.1.1", ip_type="ipv4")
    assert results == {"ip_info": "dummy_info"}


def test_given_bad_ip_address_throws_exceptions():
    client = Client("dummy_api_key")

    with pytest.raises(ValueError, match=r"IP address must be a string."):
        client.get_ip_information(1)

    with pytest.raises(ValueError, match=r"IP address must not be empty string."):
        client.get_ip_information("")

    with pytest.raises(ValueError, match=r"IP Type must be ipv4 or ipv6"):
        client.get_ip_information("1.1.1.1", ip_type="4")

    with pytest.raises(ValueError, match=r"Invalid IP address."):
        client.get_ip_information("1.1")
