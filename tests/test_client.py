import httpretty
import pytest

from silentpush.client import SilentPushExploreClient

"""Client tests"""


API_KEY = "dummy_api_key"
DOMAIN = "dummy_domain.com"


def test_when_initializing_client_with_valid_api_key_then_no_exception_thrown():
    client = SilentPushExploreClient(API_KEY)
    assert client.headers == {"X-API-KEY": API_KEY}


def test_throws_value_error_when_initializing_given_bad_api_key():
    with pytest.raises(ValueError, match=r"API key must be a string."):
        SilentPushExploreClient(1)

    with pytest.raises(ValueError, match="API key must not be empty string."):
        SilentPushExploreClient("")


@httpretty.activate
def test_get_domain_info_with_valid_domain():
    httpretty.register_uri(
        httpretty.GET,
        "https://api.silentpush.com/api/v1/merge-api/explore/domain/domaininfo/dummy_domain.com",
        body='{"status_code": 200, "error": null, "response": { "domaininfo": "dummy_info" } }'
    )
    client = SilentPushExploreClient(API_KEY)

    results = client.get_domain_information(DOMAIN)
    assert results == {"status_code": 200, "error": None, "response": {"domaininfo": "dummy_info"}}


def test_get_domain_information_with_invalid_domain_raise_exception():

    client = SilentPushExploreClient(API_KEY)

    with pytest.raises(ValueError, match=r"Domain must be a string."):
        client.get_domain_information(1)


@httpretty.activate
def test_get_domain_infratag_with_valid_domain():
    httpretty.register_uri(
        httpretty.GET,
        "https://api.silentpush.com/api/v1/merge-api/explore/domain/infratag/dummy_domain.com",
        body="""{"status_code": 200, "error": null, "response": {
                    "infratag": { "domain": "dummy_domain.com", "mode": "live",
                    "tag": "outlook.com:cloudflare.com:cloudflarenet:enom"
                    } } }"""
    )
    client = SilentPushExploreClient(API_KEY)
    assert client.get_domain_infratag(DOMAIN) == {
        "status_code": 200, "error": None,
        "response": {
            "infratag": {
                "domain": "dummy_domain.com", "mode": "live",
                "tag": "outlook.com:cloudflare.com:cloudflarenet:enom"
            }}}


def test_get_domain_infratag_with_invalid_domain_raise_exception():
    client = SilentPushExploreClient(API_KEY)

    with pytest.raises(ValueError, match=r"Domain must be a string."):
        client.get_domain_infratag(1)


@httpretty.activate
def test_get_domain_nameserver_changes_with_valid_domain():
    httpretty.register_uri(
        httpretty.GET,
        "https://api.silentpush.com/api/v1/merge-api/explore/domain/nschanges/dummy_domain.com",
        body="""{ "status_code": 200, "error": null,
                    "response": { "nschanges": { "nschanges": "dummy_changes"} } }"""
    )
    client = SilentPushExploreClient(API_KEY)
    assert client.get_domain_nameserver_changes(DOMAIN) == {"status_code": 200, "error": None,
                                                            "response": {"nschanges": {"nschanges": "dummy_changes"}}}


@httpretty.activate
def test_get_ip_information_with_valid_ip():
    httpretty.register_uri(
        httpretty.GET,
        "https://api.silentpush.com/api/v1/merge-api/explore/ipv4/ipv4info/1.1.1.1",
        body='{"ip_info": "dummy_info"}',
    )
    client = SilentPushExploreClient(API_KEY)

    results = client.get_ip_information("1.1.1.1")
    assert results == {"ip_info": "dummy_info"}

    results = client.get_ip_information("1.1.1.1", ip_type="ipv4")
    assert results == {"ip_info": "dummy_info"}


def test_given_bad_ip_address_throws_exceptions():
    client = SilentPushExploreClient(API_KEY)

    with pytest.raises(ValueError, match=r"IP address must be a string."):
        client.get_ip_information(1)

    with pytest.raises(ValueError, match=r"IP address must not be empty string."):
        client.get_ip_information("")

    with pytest.raises(ValueError, match=r"IP Type must be ipv4 or ipv6"):
        client.get_ip_information("1.1.1.1", ip_type="4")

    with pytest.raises(ValueError, match=r"Invalid IP address."):
        client.get_ip_information("1.1")
