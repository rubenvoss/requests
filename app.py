#!/Users/ruben/code/requests/venv/bin/python
# python3.11 -m venv venv --copies

import xmltodict
import requests
import sys
import logger

try:
    r = requests.get('https://www.w3schools.com/xml/plant_catalog.xml', timeout=2)
    print(f"Response is: {r.status_code} {r.reason}")
    dict = xmltodict.parse(r.text)
    plants = dict['CATALOG']['PLANT']
    for plant in plants:
        logger.debug_log(plant)
except Exception as error:
    logger.error_log(error)
    sys.exit(1)

logger.info_log("Script finished")
