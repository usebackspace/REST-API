import requests

URL = "http://127.0.0.1:8000/hero/2"

req= requests.get(url=URL)

data = req.json()    #parse the response content as JSON and stored in data variable.

print(data)