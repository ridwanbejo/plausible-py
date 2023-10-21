import os

from ..plausible import PlausibleAPI

PLAUSIBLE_HOST = os.environ.get("PLAUSIBLE_HOST", "http://localhost:8000")
PLAUSIBLE_TOKEN = os.environ.get("PLAUSIBLE_HOST")

plausible_api = PlausibleAPI(
    host=PLAUSIBLE_HOST,
    token=PLAUSIBLE_TOKEN,
)

result = plausible_api.retrieve_site(domain="tokopedia.com")
print(result)

result = plausible_api.delete_site_goal(goal_id=8, domain="tokopedia.com")
print(result)

result = plausible_api.delete_site_goal(goal_id=9, domain="tokopedia.com")
print(result)
