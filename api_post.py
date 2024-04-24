import requests
import json

URL = "http://127.0.0.1:8000/hero_create/"

data ={
    'name':'Bruce',
    'heroic_name':'Banner',
    'city':'Berlin'
}

json_data = json.dumps(data)

res= requests.post(url=URL,data=json_data)     # After sending the request the , the return response will store in req variable.

data = res.json()    #parse the response content as JSON and stored in data variable.

print(data)