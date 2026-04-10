f = open("sample.txt", "r")  #returns file object
print(f.read())

data = f.readline()         #first Line only
print(data)




f = open("sample.txt", "w")
f.write("Text to overWrite \n the complete data")



with open("sample.txt", "r") as f:          # no close required
    text = f.read()
    print(text)
    print(len(text))      # number of characters



import os
os.remove("sample2.txt")            # To delete a file



f.close()