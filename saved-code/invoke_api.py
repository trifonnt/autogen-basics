import requests

import requests
import os

url = "https://app-01.trifon.org/api/contacts";
api_key = os.environ.get("APP01_API_KEY")
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}
for value in range(122, 132):
    data = {
        "guid": "contact:{}".format(value),
        "displayName": "Contact {}".format(value),
        "firstName": "",
        "lastName": "",
        "owner": {
            "id": 1001,
            "login": "spam.trifon+101@gmail.com"
        }
    }

    response = requests.post(url, headers=headers, json=data)
    print("API invocation for value {}: status code {}".format(value, response.status_code))
    print(response.json())
