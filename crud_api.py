import requests
import json

URL = "http://127.0.0.1:8000/heroapi/"

def get_data(id=None):
    
    data ={}

    if id is not None:
        data= {'id':id}
    json_data= json.dumps(data)

    res= requests.get(url=URL, data=json_data)
    data= res.json()

    print(data)

# get_data()

def create_data():

    data={
        'name':'Bruce Banner',
        'heroic_name':'Hulk',
        'city':'NYC'
    }

    json_data = json.dumps(data)

    res = requests.post(url=URL, data=json_data)

    data = res.json()

    print(data)

# create_data()

def update():

    data={
        'id':4,
        'name':'Banner',
        'heroic_name':'hulkkkk',
        'city':'Berlinnn'
    }

    json_data = json.dumps(data)

    res = requests.put(url=URL, data=json_data)

    data = res.json()

    print(data)

# update()

def delete():

    data ={'id':3}

    json_data = json.dumps(data)

    res = requests.delete(url=URL, data=json_data)

    data = res.json()

    print(data)

delete()