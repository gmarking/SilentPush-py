import requests
from url_builder import (
    get_domain_information_request_url,
    get_ip_information_request_url,
)
from utils import IPV4
from validators import validate_api_key, validate_domain, validate_ip_address


class Client:
    """Client for interacting with Silent Push Explore API.

    PARAMETERS:
    api_key str: Your Silent Push API key.
    """

    def __init__(self, api_key: str):
        """Initialize client using provided API key."""

        self.session = requests.Session()
        self.headers = {}

        validate_api_key(api_key)
        self.headers["X-API-KEY"] = api_key

    def get_domain_information(self, domain: str) -> dict:
        """Sends a GET request to Silent Push Domain Information API endpoint.

        PARAMETERS:
        domain str: domain whos information is being requested

        RETURNS:
        A dictionary containing the Domain Information in JSON format.

        EXCEPTIONS:
        ValueError: If passed domain is invalid
        HTTPError: Thrown if any status code other than 200 is recieved
        from the request.
        """

        validate_domain(domain)

        url = get_domain_information_request_url(domain)
        result = self.session.get(url, headers=self.headers)
        if result.status_code != 200:
            result.raise_for_status()
        return result.json()

    def get_ip_information(
        self, ip_address: str, ip_type: str = IPV4, explain: bool = False
    ) -> dict:
        """Sends a GET request to Silent Push IP information API endpoint.

        PARAMETERS:
        ip_addess str: ip address whos information is being requested
        ip_type str: string specifying which type of ip address is being
        passed with a default of ipv4

        explain bool: boolean flag to indicate if we want to include
        underlying data SP uses to calculate score

        RETURNS:
        A dictionary containing the ip address information in JSON format.

        EXCEPTIONS:
        ValueError: If ip_address or ip_type is invalid.
        HTTPError: Thrown if any status code other than 200 is recieved
        from the request.
        """

        validate_ip_address(ip_address, ip_type)
        url = get_ip_information_request_url(ip_address, ip_type)
        params = {"explain": int(explain)}
        result = self.session.get(url, headers=self.headers, params=params)
        return result.json()
