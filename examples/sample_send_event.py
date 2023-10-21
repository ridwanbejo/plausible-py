from ..plausible import PlausibleAPI

plausible_api = PlausibleAPI(
    host="http://localhost:8000",
    token="x8CuaFzz4cdwz6Pv0Onkv5w9tUZd0VfWMiuFZroEAHggYe0ppEhwp84O7Csg_AYn",
)

result = plausible_api.retrieve_site(domain="tokopedia.com")
print(result)

result = plausible_api.send_event(
    domain="tokopedia.com",
    name="Payment",
    url="https://www.tokopedia.com/payment",
    user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6)",
    x_forwarded_for="127.0.0.1",
    props={"username": "John Doe", "payment_status": "success"},
    currency="IDR",
    amount="100000",
)
print(result)
