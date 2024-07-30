# Program to demonstrate integration with GitHub to fetch the 
# details of Users who created Pull requests(Active) on Kubernetes Github repo.

import requests

# Github API url
# we use k8s repo for practce purpose

url = "https://api.github.com/repos/kubernetes/kubernetes/pulls" 

# we can browse this URL in web-browser to cross verify

# Replace 'Your_Github_Username' and 'Your_Personal_Access_Token' with your GitHub credentials
"""
headers = {
    'Authorization': 'token Your_Personal_Access_Token',
    'User-Agent': 'Your_Github_Username',
    'Accept': 'application/vnd.github.v3+json'
}

response = requests.get(url,  headers=headers)

"""

# Make a GET request to fetch pull requests data from the GitHub API
response = requests.get(url)  # Add headers=headers inside get() for authentication

# To check the content-format

content_type = response.headers.get('Content-Type')

print(content_type, " \n ")

# Only if the response is successful
if response.status_code == 200:
    # Convert the JSON response to a dictionary
    pull_requests = response.json()
    # Create an empty dictionary to store PR creators and their counts
    pr_creators = {}
    # Iterate through each pull request and extract the creator's name
    for pull in pull_requests:
        creator = pull["user"]["login"]
        if creator in pr_creators:
            pr_creators[creator] += 1
        else:
            pr_creators[creator] = 1
    # Display the dictionary of PR creators and their counts
    print("PR Creators and Counts:")
    for creator, count in pr_creators.items():
        print(f"{creator}: {count} PR(s)")

else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
