city = "Bangalore"
print(city[6])

# or

city = "Bangalore"[7]
print(city)


stri = "welcome to Python"
print(len(stri))
print(stri.upper())
print(stri.lower())
print(stri + str(2))
print(stri.__contains__("p"))

# replace method
stri = "welcome to Python"
print(stri)
print(stri.replace("Python", "Java"))

# Substring
stri = "welcome to Python"
sub = stri[0 : 6]
substep = stri[0:6:2]  # [start : stop : step]
print(sub)
print(substep)

# reversing the string
print(stri[::-1])

# String Formatting
city = "nyc"
event = "magicShow"
print("welcome to %s in %s" % (event, city))  # this is called a variable place holder.

# converting String to list
list1 = stri.split()
print(list1)

# printing same format multiple times
a = "Hello"
print(a * 20)
