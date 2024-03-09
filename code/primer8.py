fileptr = open("file2.txt", "r")

for i in fileptr:
    print(i)

fileptr.close()