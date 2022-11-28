import requests

endpoint = "http://localhost:8000/v1/restaurants/84fcd602-5664-47a6-afd4-240798c6b1a7/"  # http://127.0.0.1:8000/

get_response = requests.delete(endpoint)  # HTTP Request

print(get_response.status_code, get_response.status_code == 204)

# endpoint = "http://localhost:8000/v1/employees/5eeb7bc4-895f-4858-9b10-01393df0e7ea/" #http://127.0.0.1:8000/

# get_response = requests.delete(endpoint) # HTTP Request

# print(get_response.status_code,get_response.status_code==204)
