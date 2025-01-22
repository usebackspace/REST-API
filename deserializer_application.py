import requests
import json

URL ='http://127.0.0.1:8000/marvel'

data={
    'f_name':'Abhishek',
    'heroic_name':'More'
}

json_data = json.dumps(data)
print(json_data)
res = requests.post(url=URL,data=json_data)

data= res.json()

print(data)