data = True
line = 1

with open("sample.txt", "r") as f:
    while data:
        data = f.readline()

        
        if("python" in data):
            print(f"Found python word in the file at line {line}")
            break
        line += 1
