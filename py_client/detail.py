import requests

# endpoint = "http://localhost:8000/v1/restaurants/84fcd602-5664-47a6-afd4-240798c6b1a7/" #http://127.0.0.1:8000/

# get_response = requests.get(endpoint) # HTTP Request

# print(get_response.json())

# import requests

# endpoint = "http://localhost:8000/v1/employees/c8260545-b50b-4eb2-b8c2-dfb6b2f8977e/" #http://127.0.0.1:8000/

# get_response = requests.get(endpoint) # HTTP Request

# print(get_response.json())

endpoint = "http://localhost:8000/v1/restaurants/693c44fa-397f-416c-937a-7fd1e98f6886/menu/"  # http://127.0.0.1:8000/

get_response = requests.get(endpoint)  # HTTP Request

print(get_response.json())
