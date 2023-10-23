import unittest

from plausible import PlausibleAPI


class TestMain(unittest.TestCase):
    def get_plausible_api_obj(self):
        plausible_api = PlausibleAPI(
            host="http://localhost:8000", token="12345"
        )  # nosec B106

        return plausible_api

    def test_build_url(self):
        plausible_api = self.get_plausible_api_obj()
        url = plausible_api.build_url(plausible_api.CREATE_SITE_URL)
        expected_url = plausible_api.host + plausible_api.CREATE_SITE_URL

        self.assertIs(type(url), str)
        self.assertEqual(url, expected_url)

    def test_get_url(self):
        plausible_api = self.get_plausible_api_obj()
        url = plausible_api.get_url("create-site")
        expected_url = plausible_api.host + plausible_api.CREATE_SITE_URL

        self.assertIs(type(url), str)
        self.assertEqual(url, expected_url)
