#!/Users/ruben/code/requests/venv/bin/python
# python3.11 -m venv venv --copies

import xmltodict
import requests
import sys

payload = {'username': 'ruben', 'password': 25}
try:
    r = requests.get('https://www.w3schools.com/xm/plant_catalog.xml', timeout=2)
    if r.ok:
        print(f"Response is: {r.status_code} {r.reason}")
        # print(r)
        # print(r.json())
        dict = xmltodict.parse(r.text)
        plants = dict['CATALOG']['PLANT']
        for plant in plants:
            print(plant)
    else:
        print(f"Response is: {r.status_code} {r.reason}")
except Exception as e:
    print(e)
    sys.exit(1)
