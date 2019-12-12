# Program when json is hardcoded
import requests
import json

# Endpoint url
url1 = "https://reqres.in/api/users"

#Objective : while passing payloads(not from file)
data1 = {"name": "morpheus",
        "job": "leader"}

#Posting request url
r = requests.post(url=url1,data=data1)
print(r.text)

#Load data in json format
data = json.loads(r.text)
print("\n", data)



