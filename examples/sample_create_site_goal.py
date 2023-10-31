import os

from ..plausible import PlausibleAPI

PLAUSIBLE_HOST = os.environ.get("PLAUSIBLE_HOST", "http://localhost:8000")
PLAUSIBLE_TOKEN = os.environ.get("PLAUSIBLE_HOST")

plausible_api = PlausibleAPI(
    host=PLAUSIBLE_HOST,
    token=PLAUSIBLE_TOKEN,
)

# result = plausible_api.create_site(domain="jago.com", time_zone="Asia/Jakarta")
# print(result)

result = plausible_api.create_site_goal(
    domain="jago.com", goal_type="event", event_name="Login"
)
print(result)

result = plausible_api.create_site_goal(
    domain="=jago.com", goal_type="page", page_path="/signup"
)
print(result)
