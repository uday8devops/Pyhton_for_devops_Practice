# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://udaycloudtraining.atlassian.net/rest/api/3/project"

API_TOKEN = "ATATT3xFfGF0qXvTqDVf95w3XIP8EyihqMZBc-1pfPG9kvKe9vwBj2UUxB71JEoevGm2MXrm2E4Ef2hRomt-CNhgYZ0GvzQzGClnTEaYxmWY0xnzJTqmmjNdUGkhn_v3aN_WR8_jq1kQZfWWwMu6QRWV_G486TZsHvTvcD6Hfiyth78VUDi9aBk=07B1D7F5"

auth = HTTPBasicAuth("udaycloud.training@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps({
  "key": "IND",
  "name": "python_jira",
  "projectTypeKey": "software",
  "projectTemplateKey": "com.pyxis.greenhopper.jira:gh-simplified-agility-scrum",
  "leadAccountId": "712020:a01ffdf9-aa20-4711-9047-6f58d39838b7"
})

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))