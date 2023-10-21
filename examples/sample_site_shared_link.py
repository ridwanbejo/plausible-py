from ..plausible import PlausibleAPI

plausible_api = PlausibleAPI(
    host="http://localhost:8000",
    token="x8CuaFzz4cdwz6Pv0Onkv5w9tUZd0VfWMiuFZroEAHggYe0ppEhwp84O7Csg_AYn",
)

result = plausible_api.retrieve_site(domain="tokopedia.com")
print(result)

result = plausible_api.create_site_shared_link(
    domain="tokopedia.com", name="Tokopedia Homepage"
)
print(result)
