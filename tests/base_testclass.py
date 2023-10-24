import unittest

from plausible import PlausibleAPI


class BaseTestClass(unittest.TestCase):
    def get_plausible_api_obj(self):
        plausible_api = PlausibleAPI(
            host="http://localhost:8000", token="12345"
        )  # nosec B106

        return plausible_api
