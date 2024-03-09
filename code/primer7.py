fileptr = open("file2.txt", "r")

content = fileptr.read(10)

print(type(content))

print(content)

fileptr.close()
