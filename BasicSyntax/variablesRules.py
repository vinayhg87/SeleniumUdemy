import keyword

# which lists all the keywords
print(keyword.kwlist)

a = b = c = 10
print(a)
print(b)
print(c)

a, b, c = 30, 40, 50
print(a)
print(b)
print(c)

# allowed variable names : var can start with _ or caps or small letters.
# variable names start with number or special chars are not allowed
# variable names cannot contain special chars
_test1_int = "String1"


int_num = 1022
float_num = 2340

# boolean 
bool_1 = True
bool_0 = False

print(bool_1)
print(bool_0)

# or

print(bool(0))  # false
print(bool(1))  # true
print(bool(2))  # true

c = ""
print(bool(c))  # false

c = "Test1"
print(bool(c))  # true