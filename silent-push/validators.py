import ipaddress

from utils import IPV4, IPV6

"""Some helpful functions to validate arguments passed to client"""


def validate_string(name: str, value: str) -> None:

    if not isinstance(value, str):
        raise ValueError(f"{name} must be a string.")

    if not value:
        raise ValueError(f"{name} must not be empty string.")


def validate_api_key(api_key: str) -> None:
    validate_string("API key", api_key)


def validate_domain(domain: str) -> None:
    validate_string("Domain", domain)

    # TODO: write regex to throw exception on invalid domain names
    # handling bad domains will save us from hitting api request limits as quickly

    # rule = re.compile(r"[a-zA-Z\d-]{,63}(\.[a-zA-Z\d-]{,63})*")
    # if not rule.match(domain):
    #     raise ValueError("Invalid Domain.")


def validate_ip_address(ip_address: str, ip_type: str) -> None:
    validate_string("IP address", ip_address)

    if ip_type not in {IPV4, IPV6}:
        raise ValueError("IP Type must be ipv4 or ipv6.")

    try:
        if ip_type == IPV4:
            ipaddress.IPv4Address(ip_address)
        else:
            ipaddress.IPv6Address(ip_address)
    except ipaddress.AddressValueError:
        raise ValueError("Invalid IP address.")