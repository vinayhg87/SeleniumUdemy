# length of list
list1 = ["BMW", "AUDI", "FERRARI"]
print(len(list1))

# adding data to list
list1.append("HONDA")
list1.append("BUGAATI")
list1.insert(2, "LAMBI")
print(list1)

# finding the index of a element List
x = list1.index("LAMBI")
print(x)

# removing the elements from the list
list1.pop()  # By default it removes the last element
print(list1)

list1.remove("BMW")  # it removes the specific element/s
print(list1)

# Slicing of lists
slicing = list1[0:2]
print(slicing)

slicing = list1[0:3]
print(slicing)

slicing = list1[0:4:1]
print(slicing)

slicing = list1[::-1]  # Reversing the list
print(slicing)

# sorting
print("Sorting:")
print(list1)
list1.sort()
print(list1)

# find out number of '2' in the list
list2 = [1, 3, 2, 4, 6, 2, 4, 3, 5, 6, 7, 9, 2, 43, 5, 11, 34, 2]
print(list2.count(2)) # Answer should be 4 as it has 4 times '2' has occured in list2
