#!/Users/ruben/code/requests/venv/bin/python
# python3.11 -m venv venv --copies

import xmltodict
import requests
import sys
import logger
import traceback


def request_dict(url, timeout=10):
    request = requests.get(url, timeout=timeout)
    return xmltodict.parse(request.text)

def select_plants(dict):
    plants = dict['CATALOG']['PLANT']
    return plants

try:
    dict = request_dict('https://www.w3schools.com/xml/note_error.xml', timeout=2)
except Exception as e:
    logger.exception_log(e)
    print(e)
    traceback.print_exc()
    sys.exit(1)
plants = select_plants(dict)
for plant in plants:
    logger.debug_log(plant)
    print(plant)

logger.info_log("Script finished")
