import requests
import json

# Endpoint url
url = "https://reqres.in/api/users/2"

# Request to push delete end point
x= requests.delete(url)

#Print status code after succesfully deletion
print(x.status_code)