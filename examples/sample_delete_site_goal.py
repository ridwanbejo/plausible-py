from ..plausible import PlausibleAPI

plausible_api = PlausibleAPI(
    host="http://localhost:8000",
    token="x8CuaFzz4cdwz6Pv0Onkv5w9tUZd0VfWMiuFZroEAHggYe0ppEhwp84O7Csg_AYn",
)

result = plausible_api.retrieve_site(domain="tokopedia.com")
print(result)

result = plausible_api.delete_site_goal(goal_id=8, domain="tokopedia.com")
print(result)

result = plausible_api.delete_site_goal(goal_id=9, domain="tokopedia.com")
print(result)
