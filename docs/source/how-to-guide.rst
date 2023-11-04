How To Guide
============

A. Managing sites
*****************

create site:

.. code-block:: python3

	import os

	from plausible import PlausibleAPI

	PLAUSIBLE_HOST = os.environ.get("PLAUSIBLE_HOST", "http://localhost:8000")
	PLAUSIBLE_TOKEN = os.environ.get("PLAUSIBLE_HOST")

	plausible_api = PlausibleAPI(
	    host=PLAUSIBLE_HOST,
	    token=PLAUSIBLE_TOKEN,
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


retrieve site:

.. code-block:: python3

	import os

	from plausible import PlausibleAPI

	PLAUSIBLE_HOST = os.environ.get("PLAUSIBLE_HOST", "http://localhost:8000")
	PLAUSIBLE_TOKEN = os.environ.get("PLAUSIBLE_HOST")

	plausible_api = PlausibleAPI(
	    host=PLAUSIBLE_HOST,
	    token=PLAUSIBLE_TOKEN,
	)

	result = plausible_api.retrieve_site("tokopedia.com")
	print(result)

	result = plausible_api.retrieve_site("jago.com")
	print(result)

	result = plausible_api.retrieve_site("gojek.com")
	print(result)

	result = plausible_api.retrieve_site("evermos.com")
	print(result)

	result = plausible_api.retrieve_site("efishery.com")
	print(result)

	result = plausible_api.retrieve_site("blibli.com")
	print(result)

	result = plausible_api.retrieve_site("traveloka.com")
	print(result)

update site:

.. code-block:: python3

	import os

	from plausible import PlausibleAPI

	PLAUSIBLE_HOST = os.environ.get("PLAUSIBLE_HOST", "http://localhost:8000")
	PLAUSIBLE_TOKEN = os.environ.get("PLAUSIBLE_HOST")

	plausible_api = PlausibleAPI(
	    host=PLAUSIBLE_HOST,
	    token=PLAUSIBLE_TOKEN,
	)

	result = plausible_api.update_site("jago.com", "bankjago.com")
	print(result)

	result = plausible_api.retrieve_site("bankjago.com")
	print(result)

delete site:

.. code-block:: python3

	import os

	from plausible import PlausibleAPI

	PLAUSIBLE_HOST = os.environ.get("PLAUSIBLE_HOST", "http://localhost:8000")
	PLAUSIBLE_TOKEN = os.environ.get("PLAUSIBLE_HOST")

	plausible_api = PlausibleAPI(
	    host=PLAUSIBLE_HOST,
	    token=PLAUSIBLE_TOKEN,
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
	result = plausible_api.delete_site("blibli.com")
	print(result)

	result = plausible_api.delete_site("traveloka.com")
	print(result)


B. Managing site goals
**********************

Lorem ipsum sit dolor amet


C. Sending an event
*******************

Lorem ipsum sit dolor amet


D. Get realtime visitors
************************

Lorem ipsum sit dolor amet
