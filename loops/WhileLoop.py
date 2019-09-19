
# adding data to list using while loop
print("while loop:")
list2 = []
x = 0
while x < 10:
    list2.append(x)
    x += 1
    if x == 5:
        print("continue the loop")
        continue
    if x == 8:
        print("breaking loop")
        break
print(list2)

print("*"*20)

# using else in while loop
print("using else in while loop:")
list1 = []
x = 0
while x < 10:
    list1.append(x)
    x += 1
else:
    print(list1)
    print("the loop ended in else loop")
