API_ROOT = "https://api.silentpush.com/api/v1/merge-api/"

"""Helpful functions to build Silent Push API request URLs"""


def get_domain_information_request_url(domain: str) -> str:
    """Returns the domain information url to be requested.

    :param domain: domain whos information will be requested.
    :type domain: str

    :returns: url to be sent in request
    """
    return f"{API_ROOT}explore/domain/domaininfo/{domain}"

def get_domain_infratag_request_url(domain: str) -> str:
    """Returns the domain infratag url to be requested.

    :param domain: domain whos infratag will be requested.
    :type domain: str

    :returns: url to be sent in request
    """
    return f"{API_ROOT}explore/domain/infratag/{domain}"

def get_domain_nschanges_request_url(domain: str) -> str:
    """Returns the domain name server changes url to be requested.

    :param domain: domain whos name server changes will be requested.
    :type domain: str

    :returns: url to be sent in request
    """
    return f"{API_ROOT}explore/domain/nschanges/{domain}"

def get_ip_information_request_url(ip: str, ip_type: str) -> str:
    """Returns the ip information url to be requested

    :param ip: ip address whos information will be requested
    :param ip_type: ip type of the ip address

    :returns: url to be sent in request
    """
    return f"{API_ROOT}explore/{ip_type}/{ip_type}info/{ip}"
