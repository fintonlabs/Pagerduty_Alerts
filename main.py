import requests
from typing import Dict, Any, List
from requests.models import PreparedRequest
from requests.exceptions import HTTPError

class IncidentFetcher:
    """
    A class used to fetch incidents from a RESTful API.

    ...

    Attributes
    ----------
    base_url : str
        the base URL for the API
    token : str
        the OAuth 2.0 token for API authentication
    incident_limit : int
        the maximum number of incidents to fetch

    Methods
    -------
    fetch_incidents():
        Fetches incidents from the API.
    """

    def __init__(self, base_url: str, token: str, incident_limit: int = 500):
        """
        Parameters
        ----------
        base_url : str
            The base URL for the API.
        token : str
            The OAuth 2.0 token for API authentication.
        incident_limit : int, optional
            The maximum number of incidents to fetch (default is 500).
        """

        self.base_url = base_url
        self.token = token
        self.incident_limit = incident_limit

    def fetch_incidents(self) -> List[Dict[str, Any]]:
        """
        Fetches incidents from the API.

        Returns
        -------
        list
            A list of incidents.
        """

        incidents = []
        page = 0
        size = min(500, self.incident_limit)  # API's maximum size is 500

        while len(incidents) < self.incident_limit:
            response = self._send_request(page, size)
            incidents.extend(response.json())
            page += 1

        return incidents[:self.incident_limit]

    def _send_request(self, page: int, size: int) -> PreparedRequest:
        """
        Sends a GET request to the API.

        Parameters
        ----------
        page : int
            The page number.
        size : int
            The number of incidents per page.

        Returns
        -------
        PreparedRequest
            The response from the API.
        """

        headers = {'Authorization': f'Bearer {self.token}'}
        params = {'page': page, 'size': size}
        url = f'{self.base_url}/incidents'

        response = requests.get(url, headers=headers, params=params)

        # If the response was unsuccessful, raise an HTTPError
        response.raise_for_status()

        return response

def print_incidents(incidents: List[Dict[str, Any]]) -> None:
    """
    Prints incidents to the console.

    Parameters
    ----------
    incidents : list
        A list of incidents.
    """

    for incident in incidents:
        print(f'ID: {incident["id"]}')
        print(f'Alert Content: {incident["alertContent"]}')
        print(f'Source Data: {incident["sourceData"]}')
        print()

# Example usage:
if __name__ == "__main__":
    fetcher = IncidentFetcher('https://api.example.com', 'your_token', 1000)
    incidents = fetcher.fetch_incidents()
    print_incidents(incidents)