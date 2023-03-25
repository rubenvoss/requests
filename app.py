import requests
import sys

payload = {'username': 'ruben', 'password': 25}
try:
    r = requests.get('https://httpbin.org/delay/3', auth=('ruben', 'pass'), timeout=2)
    if r.ok:
        print(f"Response is: {r.status_code} {r.reason}")
        print(r)
        print(r.json())
except Exception as e:
    print(e)
    sys.exit(1)
