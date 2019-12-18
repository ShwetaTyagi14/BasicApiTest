import requests
import json
import jsonpath
import string

def test_add_student_record():
    api_Url = "http://thetestingworldapi.com/api/studentsDetails"
    file_Path = "D:\\Shweta_Test_API\\Student_API_Project\\Post_data1.json"
    file = open (file_Path,'r')
    content =json.loads(file.read())
    response = requests.post(url=api_Url,data=content)
    print(response.text)
    print('\n')
    print(response.content)
    print('\n')
    print(response.headers)
    response_json = json.loads(response.text)
    id = jsonpath.jsonpath(response_json , 'id')
    print ("The new Student id is " + str(id[0]))

def test_update_student_record():
    api_Url ="http://thetestingworldapi.com/api/studentsDetails/150975"
    file_Path = "D:\\Shweta_Test_API\\Student_API_Project\\Put_data1.json"
    file = open(file_Path, 'r')
    content = json.loads(file.read())
    response = requests.put(url=api_Url, data=content)
    print(response.text)
    print('\n')
    print(response.content)
    print('\n')
    print(response.headers)
    response_json = json.loads(response.text)
    print(response_json)
    status = jsonpath.jsonpath(response_json, 'status')
    message = jsonpath.jsonpath(response_json, 'msg')
    assert status[0]=='true' and message[0]=='update  data success'

def  test_get_student_details():
    api_url="http://thetestingworldapi.com/api/studentsDetails/150975"
    response = requests.get(api_url)
    print(response.content)
    response_json = response.json()
    status = jsonpath.jsonpath(response_json , 'status')
    firstname = jsonpath.jsonpath(response_json , 'data.first_name')
    assert status[0]=='true' and firstname[0]=='Anshul'

def test_delete_student_record():
    api_url = "http://thetestingworldapi.com/api/studentsDetails/150975"
    response = requests.delete(api_url)
    print(response.content)
    response_json = response.json()
    print(response_json)
    status = jsonpath.jsonpath(response_json, 'status')
    message = jsonpath.jsonpath(response_json, 'msg')
    assert status[0] == 'true' and message[0] == 'Delete  data success'





