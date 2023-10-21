import os

from ..plausible import PlausibleAPI

PLAUSIBLE_HOST = os.environ.get("PLAUSIBLE_HOST", "http://localhost:8000")
PLAUSIBLE_TOKEN = os.environ.get("PLAUSIBLE_HOST")

plausible_api = PlausibleAPI(
    host=PLAUSIBLE_HOST,
    token=PLAUSIBLE_TOKEN,
)

result = plausible_api.delete_site("tokopedia.com")
print(result)

result = plausible_api.delete_site("jago.com")
print(result)

result = plausible_api.delete_site("gojek.com")
print(result)

result = plausible_api.delete_site("evermos.com")
print(result)

result = plausible_api.delete_site("efishery.com")
print(result)
result = plausible_api.delete_site("blibli.com")
print(result)

result = plausible_api.delete_site("traveloka.com")
print(result)
