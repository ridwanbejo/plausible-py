from ..plausible import PlausibleAPI


plausible_api = PlausibleAPI(
					host="http://localhost:8000",
					token="x8CuaFzz4cdwz6Pv0Onkv5w9tUZd0VfWMiuFZroEAHggYe0ppEhwp84O7Csg_AYn"
				)

result = plausible_api.update_site("jago.com", "bankjago.com")
print(result)

result = plausible_api.retrieve_site("bankjago.com")
print(result)
