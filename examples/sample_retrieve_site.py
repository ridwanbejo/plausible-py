import os

from ..plausible import PlausibleAPI

PLAUSIBLE_HOST = os.environ.get("PLAUSIBLE_HOST", "http://localhost:8000")
PLAUSIBLE_TOKEN = os.environ.get("PLAUSIBLE_HOST")

plausible_api = PlausibleAPI(
    host=PLAUSIBLE_HOST,
    token=PLAUSIBLE_TOKEN,
)

result = plausible_api.retrieve_site("tokopedia.com")
print(result)

result = plausible_api.retrieve_site("jago.com")
print(result)

result = plausible_api.retrieve_site("gojek.com")
print(result)

result = plausible_api.retrieve_site("evermos.com")
print(result)

result = plausible_api.retrieve_site("efishery.com")
print(result)

result = plausible_api.retrieve_site("blibli.com")
print(result)

result = plausible_api.retrieve_site("traveloka.com")
print(result)
