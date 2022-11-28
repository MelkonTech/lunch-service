import requests
import json

# endpoint = "http://localhost:8000/api/restaurants/" #http://127.0.0.1:8000/

# data = {
#     "name": "Florence",
#     "address": "Yerevan Jrvezh",
#     "phone_number": "+374 10 787878",
# }

# get_response = requests.post(endpoint, data=data) # HTTP Request

# print(get_response.json())

# employe_data = {
#     "first_name":"Ted",
#     "last_name": "Donat",
#     "email": "test2@email.com"
# }

# endpoint = "http://localhost:8000/api/employees/" #http://127.0.0.1:8000/

# get_response = requests.post(endpoint, data=employe_data) # HTTP Request

# print(get_response.json())

# menu_data = {
#     "restaurant":"52fd107a-11e2-4d9c-a591-13fe4efd433e",
#     "menu": json.dumps({
#     "items": [
#         {
#             "name":"coke",
#             "qty": 20,
#             "category":"drinks",
#             "sizes":["small","large"]
#         },
#         {
#             "name":"pepsi",
#             "qty": 20,
#             "category":"drinks",
#             "sizes":["small","large"]
#         },
#         {
#             "name":"water",
#             "qty": 20,
#             "category":"drinks",
#             "sizes":["small","large"]
#         },
#         {
#             "name":"hamburger",
#             "qty": 40,
#             "category":"junk food",
#             "sizes":["small","large"]
#         },
#         {
#             "name":"fries",
#             "qty": 20,
#             "category":"junk food",
#             "sizes":["small","large"]
#         },
#         {
#             "name":"pizza",
#             "qty": 20,
#             "category":"junk food",
#             "sizes":["small","large"]
#         }
#     ]
# })
# }

# endpoint = "http://localhost:8000/api/restaurants/693c44fa-397f-416c-937a-7fd1e98f6886/menu/" #http://127.0.0.1:8000/

# get_response = requests.post(endpoint, data=menu_data) # HTTP Request

# print(get_response.json())

vote_data = {"menu": "ccce6292-2253-43e0-88a3-2038ada49200", "voted_by": "2"}

endpoint = "http://localhost:8000/v1/menu/ccce6292-2253-43e0-88a3-2038ada49200/vote/"  # http://127.0.0.1:8000/

get_response = requests.post(endpoint, data=vote_data)  # HTTP Request

print(get_response.json())
