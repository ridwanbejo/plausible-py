import os

from ..plausible import PlausibleAPI

PLAUSIBLE_HOST = os.environ.get("PLAUSIBLE_HOST", "http://localhost:8000")
PLAUSIBLE_TOKEN = os.environ.get("PLAUSIBLE_HOST")

plausible_api = PlausibleAPI(
    host=PLAUSIBLE_HOST,
    token=PLAUSIBLE_TOKEN,
)

result = plausible_api.update_site("jago.com", "bankjago.com")
print(result)

result = plausible_api.retrieve_site("bankjago.com")
print(result)
