import requests
import json

# Endpoint url
url = "https://reqres.in/api/users/2"

#Code to run data from existing json file
with open ("C:\\Users\\Shweta Tyagi\\Desktop\\Documents\\data1.json") as d:
    # s=json.dumps(d)
    r= json.loads(d.read())  #for put request need to read data from file

#Posting request url
output = requests.put(url,data=r)

#Dislpaying output text
print(output.text)