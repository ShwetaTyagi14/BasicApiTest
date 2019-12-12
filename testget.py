import requests
import json
import jsonpath

# Endpoint url
url = "https://reqres.in/api/users?page=2"

# Request for get method
response = requests.get(url)

# Print response : output type is string
print(response.text)

#Convert string to json
jsonpath_response = json.loads(response.text)
print(jsonpath_response)

#Getting data
data1 = jsonpath.jsonpath(jsonpath_response,"data[0].email")
print(data1)


# # Send get request
# response = requests.get(url)
#
# # Parse reponse to json format
# json_response = json.loads(response.text)
# # print(json_response)
#
# # Fetch value using json path
# pages = jsonpath.jsonpath(json_response,"total_pages")
# print(pages[0])
#
# assert pages[0] == 3;"Wrong"