fileptr = open("file2.txt", "r")

content = fileptr.readlines()

print(content)

fileptr.close()