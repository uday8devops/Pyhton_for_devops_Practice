from flask import Flask
import requests
from requests.auth import HTTPBasicAuth
import json


# Creating a flask Application instance
app = Flask(__name__)


# Write a Decorator for API URL PATH, 
# So, that it will be verified before executing the hello function
@app.route("/createJIRA", methods=['POST'])

# write hello-world function definition
def createJIRA():
    url = "https://udaycloudtraining.atlassian.net/rest/api/3/issue"

    API_TOKEN = "ATATT3xFfGF0qXvTqDVf95w3XIP8EyihqMZBc-1pfPG9kvKe9vwBj2UUxB71JEoevGm2MXrm2E4Ef2hRomt-CNhgYZ0GvzQzGClnTEaYxmWY0xnzJTqmmjNdUGkhn_v3aN_WR8_jq1kQZfWWwMu6QRWV_G486TZsHvTvcD6Hfiyth78VUDi9aBk=07B1D7F5"

    auth = HTTPBasicAuth("udaycloud.training@gmail.com", API_TOKEN)

    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }

    payload = json.dumps({
    "fields": {
        "project": {
            "key": "IND"  # Replace with your project ID
        },
        "summary": "Main order flow broken",  # Replace with your issue summary
        "issuetype": {
            "id": "10015"  # Replace with your issue type ID
        },
        "description": {
        "content": [
            {
            "content": [
                {
                "text": "My First Jira isuue using python script.",  # Replace with your issue description
                "type": "text"
                }
            ],
            "type": "paragraph"
            }
        ],
        "type": "doc",
        "version": 1
        }
    }
    })

    response = requests.request(
    "POST",
    url,
    data=payload,
    headers=headers,
    auth=auth
    )

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
 
# To run with built-in development server provided by falsk

# To run with default port=5000
# app.run('0.0.0.0')

# To run with custom port
app.run('0.0.0.0', port=1122) 