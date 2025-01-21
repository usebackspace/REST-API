import requests

URL ='http://127.0.0.1:8000/marvel/'

res = requests.get(url=URL)

json_data =res.json()

print(json_data)