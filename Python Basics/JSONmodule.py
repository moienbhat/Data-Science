#java script object notation, similar to python dictionary(key value pairs)

import json

py_obj = {
    "name":"mo",
    "isTeacher": True}

json_str1 = json.dumps(py_obj)      # convert python object to json string

json_str = '{ "name": "Mo", "isTeacher": true}'

py_obj1 = json.loads(json_str)       # convert json string to python object

print(type(json_str))
print(type(py_obj1), py_obj1)

print(type(json_str1), json_str1)



with open("data.json", "r") as f:
    py_obj2 = json.load(f)
    print(type(py_obj2), py_obj2)


data = {
    "name": "mo",
    "age": 25,
    "isTeacher": True
}

with open("data1.json", "w") as f:
    json.dump(data, f, indent=4, sort_keys=True)          # convert python object to json string and write to file
