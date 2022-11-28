import requests
from getpass import getpass

auth_endpoint = "http://localhost:8000/auth/"  # http://127.0.0.1:8000/
username = input("Username?\n")
password = getpass("Password?\n")

auth_response = requests.post(
    auth_endpoint, json={"username": username, "password": password}
)  # HTTP Request

print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()["token"]
    headers = {"Authorization": f"Bearer {token}"}
    endpoint = "http://localhost:8000/v1/restaurants/"  # http://127.0.0.1:8000/

    get_response = requests.get(endpoint, headers=headers)  # HTTP Request

    print(get_response.json())

# endpoint = "http://localhost:8000/v1/employees/" #http://127.0.0.1:8000/

# get_response = requests.get(endpoint) # HTTP Request

# print(get_response.json())

# endpoint = "http://localhost:8000/v1/menus/" #http://127.0.0.1:8000/

# get_response = requests.get(endpoint) # HTTP Request

# print(get_response.json())
