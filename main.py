import requests
import json
from typing import Dict, Any, List

class IncidentProcessor:
    """
    A class used to interact with a RESTful API to retrieve and process incidents and alerts.

    Attributes
    ----------
    base_url : str
        The base URL for the API.
    token : str
        The bearer token for API authentication.
    incidents_limit : int
        The maximum number of incidents to retrieve.

    Methods
    -------
    get_incidents(page: int, size: int) -> Dict[str, Any]:
        Retrieves a page of incidents from the API.
    get_alerts(incident_id: str) -> Dict[str, Any]:
        Retrieves the alerts for a specific incident from the API.
    process_incidents():
        Retrieves and processes all incidents and their related alerts.
    """

    def __init__(self, base_url: str, token: str, incidents_limit: int = 500):
        """
        Constructs all the necessary attributes for the IncidentProcessor object.

        Parameters
        ----------
        base_url : str
            The base URL for the API.
        token : str
            The bearer token for API authentication.
        incidents_limit : int, optional
            The maximum number of incidents to retrieve (default is 500).
        """
        self.base_url = base_url
        self.token = token
        self.incidents_limit = incidents_limit

    def get_incidents(self, page: int, size: int) -> Dict[str, Any]:
        """
        Retrieves a page of incidents from the API.

        Parameters
        ----------
        page : int
            The page number to retrieve.
        size : int
            The number of incidents per page.

        Returns
        -------
        dict
            The JSON response from the API.
        """
        url = f"{self.base_url}/api/v1/incidents?page={page}&size={size}"
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def get_alerts(self, incident_id: str) -> Dict[str, Any]:
        """
        Retrieves the alerts for a specific incident from the API.

        Parameters
        ----------
        incident_id : str
            The ID of the incident.

        Returns
        -------
        dict
            The JSON response from the API.
        """
        url = f"{self.base_url}/api/v1/alerts/{incident_id}"
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def process_incidents(self):
        """
        Retrieves and processes all incidents and their related alerts.

        For each incident, the alerts are retrieved and the alert content and source data are printed to the console.
        """
        page = 1
        size = self.incidents_limit
        while True:
            incidents = self.get_incidents(page, size)
            if not incidents:
                break
            for incident in incidents:
                alerts = self.get_alerts(incident["id"])
                for alert in alerts:
                    print(f"Alert Content: {alert['content']}, Source Data: {alert['sourceData']}")
            page += 1


# Example usage:
processor = IncidentProcessor("https://api.example.com", "your_token")
processor.process_incidents()