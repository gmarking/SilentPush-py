from utils import API_ROOT

"""Helpful functions to build Silent Push API request URLs"""


def get_domain_information_request_url(domain: str) -> str:
    return f"{API_ROOT}explore/domain/domaininfo/{domain}"


def get_ip_information_request_url(ip: str, ip_type: str) -> str:
    return f"{API_ROOT}explore/{ip_type}/{ip_type}info/{ip}"
