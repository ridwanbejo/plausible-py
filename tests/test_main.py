from .base_testclass import BaseTestClass


class TestMain(BaseTestClass):
    def test_build_url(self):
        plausible_api = self.get_plausible_api_obj()
        url = plausible_api.build_url(plausible_api._CREATE_SITE_URL)
        expected_url = plausible_api.host + plausible_api._CREATE_SITE_URL

        self.assertIs(type(url), str)
        self.assertEqual(url, expected_url)

    def test_get_url(self):
        plausible_api = self.get_plausible_api_obj()
        url = plausible_api.get_url("create-site")
        expected_url = plausible_api.host + plausible_api._CREATE_SITE_URL

        self.assertIs(type(url), str)
        self.assertEqual(url, expected_url)
