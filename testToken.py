import requests
import sys
import pprint
import json

headers = {
    'accept': 'application/json',
}

data = {
    'grant_type': '',
    'username': 'pavel',
    'password': '1234',
    'scope': '',
    'client_id': '',
    'client_secret': '',
}

response = requests.post('http://localhost:8080/v1/login', headers=headers, data=data)

user_access_token = json.loads(response.content.decode())['access_token']
print(user_access_token)
res = requests.get('http://localhost:8080/v1/payment', headers={'Authorization': f'Bearer {user_access_token}'})

assert res.status_code == 200
pprint.pprint(
    json.loads(res.content.decode())
)

response = requests.post('http://localhost:8080/v1/login', headers=headers, data=data)

user_access_token = json.loads(response.content.decode())['access_token']
print(user_access_token)
res = requests.get('http://localhost:8080/v1/payment')

assert res.status_code == 200
pprint.pprint(
    json.loads(res.content.decode())
)