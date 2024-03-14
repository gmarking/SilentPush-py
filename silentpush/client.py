import requests

from silentpush import params_builder, url_builder, utils, validators


class SilentPushExploreClient:
    """Client for interacting with Silent Push Explore API.

    :param api_key: Your Silent Push API key.
    :type api_key: str

    :raises ValueError: If api_key is not a non-empty string.
    """

    def __init__(self, api_key: str) -> None:
        """Initialize client using provided API key."""

        self.session = requests.Session()
        self.headers = {}

        validators.validate_api_key(api_key)
        self.headers["X-API-KEY"] = api_key

    def get_domain_information(self, domain: str) -> dict:
        """Sends a GET request to Domain Information API endpoint.

        :param domain: Domain whos information is being requested.
        :type domain: str

        :returns: A dictionary containing the Domain Information in JSON
            format.

        :raises ValueError: If passed domain is invalid.
        :raises HTTPError: Thrown if any status code other than 200 is recieved
            from the request.
        """
        validators.validate_domain(domain)

        url = url_builder.get_domain_information_request_url(domain)
        result = self.session.get(url, headers=self.headers)
        if result.status_code != 200:
            result.raise_for_status()
        return result.json()

    def get_domain_infratag(self,
                            domain: str,
                            mode: str = "",
                            match: str = "",
                            as_of: str | int = "") -> dict:
        """Sends a GET request to Domain Infratag API endpoint.

        :param domain: Domain whos infratag is being requested.
        :param mode: <live|padns> build infratags from live lookup data or from PADNS data
        :param match: <self|full> handling of self-hosted infrastructure.
        :param as_of: build infratags from padns data where the as_of timestamp
            equivalent is between the first_seen and the last_seen timestamp. If passed as
            a string, must be in iso date format. If passed as an int, can be passed in 
            epoch time or as a negative int, relative time <sec> seconds ago. 

        :type domain: str
        :type mode: str
        :type match: str
        :type as_of: str | int

        :returns: A dictionary containing the Domain infratag in JSON
            format.

        :raises ValueError: If passed domain is invalid.
        :raises HTTPError: Thrown if any status code other than 200 is recieved
            from the request.
        """
        validators.validate_domain(domain)

        url = url_builder.get_domain_infratag_request_url(domain)
        params = params_builder.build_infratag_params(mode, match, as_of)
        result = self.session.get(url, headers=self.headers, params=params)
        if result.status_code != 200:
            result.raise_for_status()
        return result.json()

    def get_domain_nameserver_changes(self, domain: str, summary: bool = False) -> dict:
        """Sends a GET request to Domain name server changes API endpoint.

        :param domain: Domain whos name server changes is being requested.
        :param summary: Flag to indicate return of results summary only. 
        :type domain: str
        :type summary: bool

        :returns: A dictionary containing the Domain infratag in JSON
            format.

        :raises ValueError: If passed domain is invalid.
        :raises HTTPError: Thrown if any status code other than 200 is recieved
            from the request.
        """
        validators.validate_domain(domain)

        url = url_builder.get_domain_nschanges_request_url(domain)
        params = {"summary": int(summary)}
        result = self.session.get(url, headers=self.headers, params=params)
        if result.status_code != 200:
            result.raise_for_status()
        return result.json()

    def get_ip_information(
        self, ip_address: str, ip_type: str = utils.IPV4, explain: bool = False
    ) -> dict:
        """Sends a GET request to Silent Push IP information API endpoint.

        :param ip_addess: IP address whos information is being requested.
        :param ip_type: Type of ip address being passed with a default of ipv4.
        :param explain: Flag to indicate if we want to include
            underlying data SP uses to calculate score.

        :type ip_address: str
        :type ip_type: str
        :type explain: bool

        :returns: A dictionary containing the ip address information in JSON
            format.

        :raises ValueError: If ip_address or ip_type is invalid.
        :raises HTTPError: Thrown if any status code other than 200 is recieved
            from the request.
        """
        validators.validate_ip_address(ip_address, ip_type)

        url = url_builder.get_ip_information_request_url(ip_address, ip_type)
        params = {"explain": int(explain)}
        result = self.session.get(url, headers=self.headers, params=params)
        return result.json()
