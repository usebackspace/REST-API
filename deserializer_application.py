
import requests
import json
URL ='http://127.0.0.1:8000/newmarvel/'

data={
    'f_name':'Natasha Romanoff',
    'heroic_name':'black widow'
}

json_data = json.dumps(data)

response = requests.post(url=URL, data=json_data)

data=response.json()

print(data)