import json
import requests

# Endpoint url
URL = "https://reqres.in/api/register"

#Code to run data from existing json file
with open ("C:\\Users\\Shweta Tyagi\\Desktop\\data.json") as d:
    x = json.load(d)
print(x)

#Posting request url
output = requests.post(url = URL, data = x)

#Dislpaying output text
print(output.text)