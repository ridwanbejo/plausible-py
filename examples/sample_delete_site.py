from ..plausible import PlausibleAPI


plausible_api = PlausibleAPI(
					host="http://localhost:8000",
					token="x8CuaFzz4cdwz6Pv0Onkv5w9tUZd0VfWMiuFZroEAHggYe0ppEhwp84O7Csg_AYn"
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
\
result = plausible_api.delete_site("blibli.com")
print(result)

result = plausible_api.delete_site("traveloka.com")
print(result)