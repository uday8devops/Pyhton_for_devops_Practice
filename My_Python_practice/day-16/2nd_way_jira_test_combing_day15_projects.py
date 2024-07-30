from flask import Flask, request, jsonify
import requests
from requests.auth import HTTPBasicAuth
import json

app = Flask(__name__)

#GITHUB_SECRET = os.getenv("GITHUB_SECRET")
JIRA_URL = "https://udaycloudtraining.atlassian.net/rest/api/3/issue"
JIRA_USER = "udaycloud.training@gmail.com"
JIRA_TOKEN = "ATATT3xFfGF0qXvTqDVf95w3XIP8EyihqMZBc-1pfPG9kvKe9vwBj2UUxB71JEoevGm2MXrm2E4Ef2hRomt-CNhgYZ0GvzQzGClnTEaYxmWY0xnzJTqmmjNdUGkhn_v3aN_WR8_jq1kQZfWWwMu6QRWV_G486TZsHvTvcD6Hfiyth78VUDi9aBk=07B1D7F5"
JIRA_PROJECT_KEY = "IND"


'''
def verify_signature(payload, signature):

    """
    Verifies the GitHub webhook payload signature.
    Ensures the payload is from GitHub and has not been tampered with.

    Args:
        payload (bytes): The raw payload from GitHub.
        signature (str): The signature from the 'X-Hub-Signature' header.

    Returns:
        bool: True if the signature is valid, False otherwise.
    """


    import hmac
    import hashlib
    secret = bytes(GITHUB_SECRET, 'utf-8')
    computed_signature = 'sha1=' + hmac.new(secret, payload, hashlib.sha1).hexdigest()
    return hmac.compare_digest(computed_signature, signature)

'''
@app.route("/webhook", methods=["POST"])
def webhook():

    # Get the raw payload and the GitHub signature from the headers
    #payload = request.get_data()
    #signature = request.headers.get('X-Hub-Signature')

    # Verify the request signature
    #if not verify_signature(payload, signature):
    #    return "Signature verification failed", 400

    # Get the event type from the headers
    #event = request.headers.get('X-GitHub-Event')

    # Process 'issue_comment' events
    #if event == "issue_comment":
    data = request.json
    comment = data["comment"]["body"]

    # Check if the comment contains '/jira'
    if "/jira" in comment:
        issue = data["issue"]
        print(comment, " :: ", issue["title"], " :: ", issue["body"])
        create_jira_ticket(issue)
    else:
        print("can not create Ticket, please comment /jira")

    return "OK", 200

# Function to convert plain text to Atlassian Document Format (ADF)
def convert_to_adf(text):
    return {
        "type": "doc",
        "version": 1,
        "content": [
            {
                "type": "paragraph",
                "content": [
                    {
                        "type": "text",
                        "text": text
                    }
                ]
            }
        ]
    }

# Function to create Jira Ticket 
def create_jira_ticket(issue):
    #API_TOKEN = "ATATT3xFfGF0qXvTqDVf95w3XIP8EyihqMZBc-1pfPG9kvKe9vwBj2UUxB71JEoevGm2MXrm2E4Ef2hRomt-CNhgYZ0GvzQzGClnTEaYxmWY0xnzJTqmmjNdUGkhn_v3aN_WR8_jq1kQZfWWwMu6QRWV_G486TZsHvTvcD6Hfiyth78VUDi9aBk=07B1D7F5"

    auth = HTTPBasicAuth(JIRA_USER, JIRA_TOKEN)


    # Set the headers for the JIRA API request
    headers = {
        "Accept": "application/json",
        #"Content-Type": "application/json"
        #"Authorization": f"Basic {JIRA_USER}:{JIRA_TOKEN}"
    }

    # Prepare the JIRA issue data
    issue_data = {
        "fields": {
            "project": {
                "key": JIRA_PROJECT_KEY
            },
            "summary": issue["title"],
            "description": convert_to_adf(issue["body"]),
            "issuetype": {
                "name": "Task"
            }
        }
    }

    # Send a POST request to the JIRA API to create the issue
    response = requests.post(f"{JIRA_URL}", headers=headers, json=issue_data, auth=auth)

    # Check if the JIRA ticket was created successfully
    if response.status_code != 201:
        print(f"Failed to create JIRA ticket: {response.content}")

if __name__ == "__main__":
    
     # Run the Flask app on port 5000
    app.run('0.0.0.0', port=5000, debug=True)
