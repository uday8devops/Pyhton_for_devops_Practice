my_dictionary = {
    "name": "uday",
    "id": "123",
    "calss": "devops"
}
del my_dictionary["id"]
my_dictionary["from"] = "KPHB"
my_dictionary["id"] = 1122


# Iterate through the dictionary and print details if name is "uday"
found = False
for key, value in my_dictionary.items():
    if key == "name" and value == "anil":
        found = True
        break

if found:
    print("Details for 'name': 'uday'")
    for key, value in my_dictionary.items():
        print(f"{key}: {value}")
else:
    print("No details found")