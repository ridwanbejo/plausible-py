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
