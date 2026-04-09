dict = {
    "name" : "Moien",
    "age" : 22
}

print(type(dict))
print(dict["name"])

dict["age"] = 23
print(dict["age"])              #Error if key not found

print(dict.keys())
print(dict.values())
print(dict.items())
print(dict.get("name"))             #Returns None if no key found
dict.update({
    "city" : "Delhi"
})

print(dict)

