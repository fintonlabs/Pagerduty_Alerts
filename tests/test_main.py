import pytest
from main import IncidentFetcher

def test_fetch_incidents():
    fetcher = IncidentFetcher('https://api.example.com', 'your_token', 1000)
    incidents = fetcher.fetch_incidents()
    assert len(incidents) <= 1000
    for incident in incidents:
        assert 'id' in incident
        assert 'alertContent' in incident
        assert 'sourceData' in incident