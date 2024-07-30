import requests


# we use k8s repo for practce purpose

reply = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls") 
# we can browse this URL in web-browser to cross verify

# test -1
# print(reply)
#
#test - 2
#print(reply.status_code)

details = reply.json() # by using this ".json()"  by deafult we will get list of dictionaries

# print(details[0]["id"])

# print(details[0]["user"]["login"]) # for single user

for i in range(len(details)):
    print(details[i]["user"]["login"])


