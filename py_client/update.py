import requests
import json

endpoint = "http://localhost:8000/api/restaurants/84fcd602-5664-47a6-afd4-240798c6b1a7/"  # http://127.0.0.1:8000/

data = {"name": "Pandok"}
get_response = requests.patch(endpoint, json=data)  # HTTP Request

print(get_response.json())

endpoint = "http://localhost:8000/api/employees/c8260545-b50b-4eb2-b8c2-dfb6b2f8977e/"  # http://127.0.0.1:8000/

data = {"first_name": "Denny"}
get_response = requests.patch(endpoint, json=data)  # HTTP Request

print(get_response.json())

endpoint = "http://localhost:8000/api/restaurants/693c44fa-397f-416c-937a-7fd1e98f6886/menu/ccce6292-2253-43e0-88a3-2038ada49200/"  # http://127.0.0.1:8000/

menu_data = {
    "menu": json.dumps(
        {
            "item": [
                {
                    "name": "coke",
                    "qty": 20,
                    "category": "drinks",
                    "sizes": ["small", "large"],
                },
                {
                    "name": "pepsi",
                    "qty": 20,
                    "category": "drinks",
                    "sizes": ["small", "large"],
                },
                {
                    "name": "water",
                    "qty": 20,
                    "category": "drinks",
                    "sizes": ["small", "large"],
                },
                {
                    "name": "hamburger",
                    "qty": 40,
                    "category": "junk food",
                    "sizes": ["small", "large"],
                },
                {
                    "name": "fries",
                    "qty": 20,
                    "category": "junk food",
                    "sizes": ["small", "large"],
                },
                {
                    "name": "pizza",
                    "qty": 20,
                    "category": "junk food",
                    "sizes": ["small", "large"],
                },
            ]
        }
    )
}
get_response = requests.patch(endpoint, json=menu_data)  # HTTP Request

print(get_response.json())
