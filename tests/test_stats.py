from unittest.mock import MagicMock, patch

from .base_testclass import BaseTestClass


class TestStats(BaseTestClass):
    @patch("plausible.requests")
    def test_create_site(self, mock_requests):
        # mock the response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {}

        # specify the return value of the get() method
        mock_requests.get.return_value = mock_response

        plausible_api = self.get_plausible_api_obj()

        result = plausible_api.get_realtime_visitors(domain="tokopedia.com")

        self.assertIs(type(result), dict)
        self.assertEqual(result["status_code"], 200)
        self.assertIs(type(result["response"]), dict)
