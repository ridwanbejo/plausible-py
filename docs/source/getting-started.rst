Getting Started
===============

A. Install from PIP
*******************

Lorem ipsum sit dolor amet

.. code-block:: shell

   $ pip install plausible-py


B. Initiate plausible-py on your Python code
********************************************

Lorem ipsum sit dolor amet

.. code-block:: python3

   	import os

	from plausible import PlausibleAPI

	PLAUSIBLE_HOST = os.environ.get("PLAUSIBLE_HOST", "http://localhost:8000")
	PLAUSIBLE_TOKEN = os.environ.get("PLAUSIBLE_HOST")

	plausible_api = PlausibleAPI(
	    host=PLAUSIBLE_HOST,
	    token=PLAUSIBLE_TOKEN,
	)
