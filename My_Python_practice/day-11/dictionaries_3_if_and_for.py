my_dictionary = {
    "name": "uday",
    "id": "123",
    "calss": "devops"
}
del my_dictionary["id"]
my_dictionary["from"] = "KPHB"
my_dictionary["id"] = 1122

'''

if "from" in my_dictionary:
    print("Name: is present")
else:
    print("no such key-name")

'''

for key, value in my_dictionary.items():
    print(f"{key}: {value}")