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

print("*"*20)

def cityName(name):
    count = 0
    citylist = ["NEW YORK", "BANGALORE", "PARIS", "BERLIN", "TOKYO"]
    for city in citylist:
        if city.lower() == str(name).lower():
            print("%s found in the list" % name)
            count = count+1
    if count == 0:
        print("%s not found in the list" % name)

cityName('NEW YORK')

print("*"*20)

# positional Parameters
print("positional Parameters")
def sum_num1(a=1, b=2):
    return a + b

print(sum_num1())  # if there are no parameters, then it will consider the values defined in the method signature.
print(sum_num1(2,3))