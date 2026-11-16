import os
import json
import msal
import requests
from dotenv import load_dotenv

load_dotenv()

TENANT_ID = os.getenv("TENANT_ID")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
SCOPE = ["https://graph.microsoft.com/.default"]

GROUP_PORTS = {
    "IT": 3129,
    "HR": 3130,
    "Finance": 3131
}

app = msal.ConfidentialClientApplication(
    CLIENT_ID,
    authority=AUTHORITY,
    client_credential=CLIENT_SECRET
)

result = app.acquire_token_for_client(scopes=SCOPE)

if "access_token" not in result:
    print("Authentication failed")
    print(result.get("error_description"))
    exit(1)

headers = {
    "Authorization": "Bearer " + result["access_token"]
}

url = (
    "https://graph.microsoft.com/v1.0/users"
    "?$select=id,displayName,userPrincipalName"
)

employee_map = {}

while url:
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Graph error:", response.status_code)
        print(response.text)
        exit(1)

    data = response.json()

    for user in data.get("value", []):
        email = user["userPrincipalName"].lower()

        groups_url = (
            f"https://graph.microsoft.com/v1.0/users/{user['id']}/memberOf"
            "?$select=displayName"
        )

        group_response = requests.get(groups_url, headers=headers)

        if group_response.status_code != 200:
            print("Could not read groups for:", email)
            continue

        groups = group_response.json().get("value", [])

        for group in groups:
            group_name = group.get("displayName")

            if group_name in GROUP_PORTS:
                employee_map[email] = {
                    "name": user["displayName"],
                    "group": group_name,
                    "port": GROUP_PORTS[group_name]
                }
                break

    url = data.get("@odata.nextLink")

with open("group_map.json", "w") as file:
    json.dump(employee_map, file, indent=4)

print("\nEmployee mapping generated:")

for email, details in employee_map.items():
    print(
        email,
        "->",
        details["group"],
        "->",
        details["port"]
    )

print("\nSaved to group_map.json")