from unittest.mock import MagicMock, patch

from .base_testclass import BaseTestClass


class TestSite(BaseTestClass):
    domain = "tokopedia.com"
    time_zone = "Asia/Jakarta"

    @patch("plausible.requests")
    def test_create_site(self, mock_requests):
        # mock the response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "domain": self.domain,
            "timezone": self.time_zone,
        }

        # specify the return value of the get() method
        mock_requests.post.return_value = mock_response

        plausible_api = self.get_plausible_api_obj()

        result = plausible_api.create_site(self.domain, self.time_zone)

        self.assertIs(type(result), dict)
        self.assertEqual(result["status_code"], 200)
        self.assertIs(type(result["response"]), dict)
        self.assertEqual(result["response"]["domain"], self.domain)
        self.assertEqual(result["response"]["timezone"], self.time_zone)

    @patch("plausible.requests")
    def test_retrieve_site(self, mock_requests):
        # mock the response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "domain": self.domain,
            "timezone": self.time_zone,
        }

        # specify the return value of the get() method
        mock_requests.get.return_value = mock_response

        plausible_api = self.get_plausible_api_obj()

        result = plausible_api.retrieve_site(self.domain)

        self.assertIs(type(result), dict)
        self.assertEqual(result["status_code"], 200)
        self.assertIs(type(result["response"]), dict)
        self.assertEqual(result["response"]["domain"], self.domain)
        self.assertEqual(result["response"]["timezone"], self.time_zone)

    @patch("plausible.requests")
    def test_update_site(self, mock_requests):
        new_domain = "neo-tokopedia.com"

        # mock the response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "domain": new_domain,
            "timezone": self.time_zone,
        }

        # specify the return value of the get() method
        mock_requests.put.return_value = mock_response

        plausible_api = self.get_plausible_api_obj()

        result = plausible_api.update_site(self.domain, new_domain)

        self.assertIs(type(result), dict)
        self.assertEqual(result["status_code"], 200)
        self.assertIs(type(result["response"]), dict)
        self.assertEqual(result["response"]["domain"], new_domain)
        self.assertEqual(result["response"]["timezone"], self.time_zone)

    @patch("plausible.requests")
    def test_delete_site(self, mock_requests):
        # mock the response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "deleted": "true",
        }

        # specify the return value of the get() method
        mock_requests.delete.return_value = mock_response

        plausible_api = self.get_plausible_api_obj()

        result = plausible_api.delete_site(self.domain)

        self.assertIs(type(result), dict)
        self.assertEqual(result["status_code"], 200)
        self.assertIs(type(result["response"]), dict)
        self.assertEqual(result["response"]["deleted"], "true")

    @patch("plausible.requests")
    def test_create_site_goal(self, mock_requests):
        # mock the response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "domain": self.domain,
            "timezone": self.time_zone,
            "id": "1",
            "goal_type": "event",
            "event_name": "Signup",
            "page_path": None,
        }

        # specify the return value of the get() method
        mock_requests.put.return_value = mock_response

        plausible_api = self.get_plausible_api_obj()

        result = plausible_api.create_site_goal(
            domain=self.domain, goal_type="event", event_name="Signup"
        )

        self.assertIs(type(result), dict)
        self.assertEqual(result["status_code"], 200)
        self.assertIs(type(result["response"]), dict)
        self.assertEqual(result["response"]["domain"], self.domain)
        self.assertEqual(result["response"]["goal_type"], "event")
        self.assertEqual(result["response"]["event_name"], "Signup")

    @patch("plausible.requests")
    def test_delete_site_goal(self, mock_requests):
        # mock the response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "deleted": "true",
        }

        # specify the return value of the get() method
        mock_requests.delete.return_value = mock_response

        plausible_api = self.get_plausible_api_obj()

        result = plausible_api.delete_site_goal(1, self.domain)

        self.assertIs(type(result), dict)
        self.assertEqual(result["status_code"], 200)

    @patch("plausible.requests")
    def test_create_site_shared_link(self, mock_requests):
        shared_link_name = "Tokopedia"

        # mock the response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "name": shared_link_name,
            "url": "https://plausible.io/share/tokopedia.com?auth=abc123",
        }

        # specify the return value of the get() method
        mock_requests.put.return_value = mock_response

        plausible_api = self.get_plausible_api_obj()

        result = plausible_api.create_site_shared_link(
            domain=self.domain, name=shared_link_name
        )

        self.assertIs(type(result), dict)
        self.assertEqual(result["status_code"], 200)
        self.assertIs(type(result["response"]), dict)
        self.assertEqual(result["response"]["name"], shared_link_name)
        self.assertEqual(
            result["response"]["url"],
            "https://plausible.io/share/tokopedia.com?auth=abc123",
        )
