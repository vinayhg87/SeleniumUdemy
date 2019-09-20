
myList = ["hello", "hello1", "Hello2", "hello3"]
writeOperation = open("testInput.txt", "w")
for listItem in myList:
    writeOperation.writelines(listItem + '\n')
writeOperation.close()


readOperation = open("testInput.txt", "r")
lines = readOperation.read().splitlines()
for i in lines:
    if str(i) == "hello1":
        print("pattern")

readOperation.close()


readOperation = open("testInput.txt", "r")
print(readOperation.read())
readOperation.close()


