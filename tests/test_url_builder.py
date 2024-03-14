import silentpush.url_builder as builder

"""Url builder tests"""

DOMAIN = "dummy.com"
IPV4 = "1.1.1.1"
IP4_TYPE = "ipv4"
IPV6 = "2606:4700:4700::1111"
IP6_TYPE = "ipv6"


def test_get_domain_information_request_url():
    expected_url = "https://api.silentpush.com/api/v1/merge-api/explore/domain/domaininfo/dummy.com"
    assert builder.get_domain_information_request_url(DOMAIN) == expected_url


def test_get_domain_infratag_request_url():
    expected_url = "https://api.silentpush.com/api/v1/merge-api/explore/domain/infratag/dummy.com"
    assert builder.get_domain_infratag_request_url(DOMAIN) == expected_url


def test_get_domain_nschanges_request_url():
    expected_url = "https://api.silentpush.com/api/v1/merge-api/explore/domain/nschanges/dummy.com"
    assert builder.get_domain_nschanges_request_url(DOMAIN) == expected_url


def test_get_ip_information_request_url_IPV4():
    expected_url = "https://api.silentpush.com/api/v1/merge-api/explore/ipv4/ipv4info/1.1.1.1"
    assert builder.get_ip_information_request_url(IPV4, IP4_TYPE) == expected_url


def test_get_ip_information_request_url_IPV6():
    expected_url = "https://api.silentpush.com/api/v1/merge-api/explore/ipv6/ipv6info/2606:4700:4700::1111"
    assert builder.get_ip_information_request_url(IPV6, IP6_TYPE) == expected_url
