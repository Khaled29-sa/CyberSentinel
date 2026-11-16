import os
import msal
import requests
from dotenv import load_dotenv

load_dotenv()

TENANT_ID = os.getenv("TENANT_ID")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
SCOPE = ["https://graph.microsoft.com/.default"]

app = msal.ConfidentialClientApplication(
    CLIENT_ID,
    authority=AUTHORITY,
    client_credential=CLIENT_SECRET
)

result = app.acquire_token_for_client(scopes=SCOPE)

if "access_token" not in result:
    print("Authentication failed")
    print(result.get("error"))
    print(result.get("error_description"))
    exit(1)

headers = {
    "Authorization": "Bearer " + result["access_token"]
}

users_url = "https://graph.microsoft.com/v1.0/users?$select=id,displayName,userPrincipalName"

response = requests.get(users_url, headers=headers)

if response.status_code != 200:
    print("Failed to retrieve users:", response.status_code)
    print(response.text)
    exit(1)

for user in response.json().get("value", []):

    print("\nEmployee:", user["displayName"])
    print("Email:", user["userPrincipalName"])

    groups_url = (
        f"https://graph.microsoft.com/v1.0/users/{user['id']}/memberOf"
        "?$select=displayName"
    )

    group_response = requests.get(groups_url, headers=headers)

    if group_response.status_code == 200:
        groups = group_response.json().get("value", [])

        for group in groups:
            print("Group:", group.get("displayName"))
    else:
        print("Failed to retrieve groups:", group_response.status_code)