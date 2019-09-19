# defining a method which has the addition functionality
def sum_num(a, b):
    c = a + b
    return c


# list Creation:
list1 = [3, 5, 2, 1, 4, 5, 6]
list2 = [5, 6, 3, 2, 5, 2, 5]

# Iterating lists using zip method to perform addition.
for l1, l2 in zip(list1, list2):
    print(sum_num(l1, l2))  # calling methods

print("*" * 20)


def cityName(name):
    count = 0
    citylist = ["NEW YORK", "BANGALORE", "PARIS", "BERLIN", "TOKYO"]
    for city in citylist:
        if city.lower() == str(name).lower():
            print("%s found in the list" % name)
            count = count + 1
    if count == 0:
        print("%s not found in the list" % name)


cityName('NEW YORK')

print("*" * 20)

# positional Parameters
print("positional Parameters")


def sum_num1(a=1, b=2):
    return a + b


print(sum_num1())  # if there are no parameters, then it will consider the values defined in the method signature.
print(sum_num1(2, 3))

print("*" * 20)


# n number of arguments in a method
def sum_num2(*args):
    print(list(args))  # converting arguments to list
    print(max(args))
    print(min(args))


sum_num2(2, 3, 4, 3, 2, 5, 4, 7, 7, 1, 8, 4, 34, 45, 43, 4, 3)

print("*" * 20)

# data types identification
print(type(99.9))
print(type("hello"))
print(type(True))
print(type(1))
print(type(list1))

print("*" * 20)
# Exercise : Sorting the Data in list3


list3 = [3, 5, 2, 1, 6, 4, 8, 7]
print("The length of list3 is %d" % len(list3))
for i in range(0, len(list3) - 1):
    for j in range(i + 1, len(list3) - 1):
        if list3[i] > list3[j]:
            temp = 0
            temp = list3[i]
            list3[i] = list3[j]
            list3[j] = temp

print(list3)
