import unittest
from unittest.mock import patch
from incident_processor import IncidentProcessor

class TestIncidentProcessor(unittest.TestCase):
    @patch('requests.get')
    def test_get_incidents(self, mock_get):
        mock_get.return_value.json.return_value = {'incidents': []}
        processor = IncidentProcessor("https://api.example.com", "your_token")
        incidents = processor.get_incidents(1, 10)
        self.assertEqual(incidents, {'incidents': []})

    @patch('requests.get')
    def test_get_alerts(self, mock_get):
        mock_get.return_value.json.return_value = {'alerts': []}
        processor = IncidentProcessor("https://api.example.com", "your_token")
        alerts = processor.get_alerts("incident_id")
        self.assertEqual(alerts, {'alerts': []})

if __name__ == '__main__':
    unittest.main()