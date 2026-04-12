squares = []

for i in range(6):
    squares.append(i*i)

print(squares)

squares = [i*i for i in range(6) if i%2!=0]           #list comprehension

print(squares)

list = [-2,-4,4,7,-8,-9,10]
pos = [0 if val < 0 else val for val in list]          # if value is negative then replace with 0
print(pos)

word = ["hello", "World", "Python"]
upper = [val.upper() for val in word]
print(upper)