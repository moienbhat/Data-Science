marks = [57, 89, 67, 58]
print(marks)
print(marks[1])
print(marks[2:len(marks)])

marks[2] = 70
print(marks)


marks.append(89)
marks.insert(2, 61)
marks.sort(reverse = True)
marks.reverse()

print(marks)

for val in marks:
    print(val)

