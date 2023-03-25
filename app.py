import requests
import sys

payload = {'username': 'ruben', 'password': 25}
try:
    r = requests.post('https://httpbin.org/post', data=payload)
# r = requests.get('https://htpbin.org/post', params=payload)
except Exception as e:
    print(e)
    sys.exit(1)
else:
    print(r.url)
    print(r.text)
    print(r.json())
# print(r.text)
# print(help(r))
