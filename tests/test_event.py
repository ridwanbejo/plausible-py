from unittest.mock import MagicMock, patch

from .base_testclass import BaseTestClass


class TestEvent(BaseTestClass):
    @patch("plausible.requests")
    def test_create_site(self, mock_requests):
        # mock the response
        mock_response = MagicMock()
        mock_response.status_code = 202
        mock_response.json.return_value = {}

        # specify the return value of the get() method
        mock_requests.post.return_value = mock_response

        plausible_api = self.get_plausible_api_obj()

        result = plausible_api.send_event(
            domain="tokopedia.com",
            name="Payment",
            url="https://www.tokopedia.com/payment",
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6)",
            x_forwarded_for="127.0.0.1",
            props={"username": "John Doe", "payment_status": "success"},
            currency="IDR",
            amount="100000",
        )

        self.assertIs(type(result), dict)
        self.assertEqual(result["status_code"], 202)
        self.assertIs(type(result["response"]), dict)
