# my_tuple is immutable and hence we cannot add any data to tuple
my_tuple = (2,3,4,56,4,2,4)
print(my_tuple[3])

my_tuple.index(3)  # to find the index of a element

tuple_slicing = my_tuple[1:5]
print(tuple_slicing)

print("the length of tuple is %d" % len(my_tuple))

# how many times the numbers are repeated in a tuple
print("no of times 4 present in tuple is %d" % (my_tuple.count(4)))