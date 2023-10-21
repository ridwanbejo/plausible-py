from ..plausible import PlausibleAPI

plausible_api = PlausibleAPI(
    host="http://localhost:8000",
    token="x8CuaFzz4cdwz6Pv0Onkv5w9tUZd0VfWMiuFZroEAHggYe0ppEhwp84O7Csg_AYn",
)

# result = plausible_api.create_site(domain="tokopedia.com", time_zone="Asia/Jakarta")
# print(result)

result = plausible_api.create_site_goal(
    domain="tokopedia.com", goal_type="event", event_name="Login"
)
print(result)

result = plausible_api.create_site_goal(
    domain="tokopedia.com", goal_type="page", page_path="/signup"
)
print(result)
