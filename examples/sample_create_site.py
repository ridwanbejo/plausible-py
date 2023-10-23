import os

from ..plausible import PlausibleAPI

PLAUSIBLE_HOST = os.environ.get("PLAUSIBLE_HOST", "http://localhost:8000")
PLAUSIBLE_TOKEN = os.environ.get("PLAUSIBLE_TOKEN")

plausible_api = PlausibleAPI(
    host=PLAUSIBLE_HOST,
    token=PLAUSIBLE_TOKEN,
)

result = plausible_api.create_site("tokopedia.com", "Asia/Jakarta")
print(result)

result = plausible_api.create_site("jago.com", "Asia/Jakarta")
print(result)

result = plausible_api.create_site("gojek.com", "Asia/Jakarta")
print(result)

result = plausible_api.create_site("evermos.com", "Asia/Jakarta")
print(result)

result = plausible_api.create_site("efishery.com", "Asia/Jakarta")
print(result)

result = plausible_api.create_site("blibli.com", "Asia/Jakarta")
print(result)

result = plausible_api.create_site("traveloka.com", "Asia/Jakarta")
print(result)
