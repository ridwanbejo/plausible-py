import os

from ..plausible import PlausibleAPI

PLAUSIBLE_HOST = os.environ.get("PLAUSIBLE_HOST", "http://localhost:8000")
PLAUSIBLE_TOKEN = os.environ.get("PLAUSIBLE_HOST")

plausible_api = PlausibleAPI(
    host=PLAUSIBLE_HOST,
    token=PLAUSIBLE_TOKEN,
)

result = plausible_api.retrieve_site(domain="jago.com")
print(result)

result = plausible_api.get_realtime_visitors(domain="jago.com")
print(result)
