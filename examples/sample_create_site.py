from ..plausible import PlausibleAPI

plausible_api = PlausibleAPI(
    host="http://localhost:8000",
    token="x8CuaFzz4cdwz6Pv0Onkv5w9tUZd0VfWMiuFZroEAHggYe0ppEhwp84O7Csg_AYn",
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
