
myList = ["hello", "hello1", "Hello2", "hello3"]

with open("testInput1.txt", "w") as file1, open("testInput2.txt", "w") as file2:
    for items in myList:
        file1.write(items+'\n')
        file2.write(items+'\n')
file1.close()
file2.close()

with open("testInput1.txt", "r") as file1, open("testInput2.txt", "r") as file2:
    for line1, line2 in zip(file1, file2):
        if line1 == line2:
            print("pattern")