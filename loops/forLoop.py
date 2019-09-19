
# normal for loop for string
myString = "test1welcome"
for ch in myString:
    if ch == 'm':
        print("M", end="")
    print(ch, end="")

print("*"*30)

# list for loop
list1 = ["BMW", "AUDI", "FERRARI"]
for l in list1:
    print(l)

print("*"*30)

# dictionary for loop
cars = {"CarName": "BMW", "model": "i8", "make": 2018}
for k in cars:
    print(cars[k])

print("*"*40)

# dictionary for loop with key and value
for k, v in cars.items():
    if k == "model":
        print(v)

print("*"*40)

# range. this function is used only for integers or increment
for i in range(10):
    print(i)

print("*"*30)

# to print even numbers or it prints with 2 steps.
for i in range(0,10,2):
    print(i)

print("*"*30)
# to print from 10 to 1 or decrement
for i in range(10,0,-1):
    print(i)