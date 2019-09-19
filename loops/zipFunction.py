# Iterating multiple lists at the same time:
# Zip method will work based on the size of the lists and it considers the list which has smaller size.
# For example, list2 has smaller size and hence zip method will consider list2 size.
# So zip iterates till '4534' in list2 and same length will be considered for list1 .So zip iterates till '2' in list1.

list1 = [1, 42213, 2, 42223, 6, 1, 1]
list2 = [43, 564, 4534]

for l1,l2 in zip(list1,list2):
    if l1 > l2:
        print(l1)
    else:
        print(l2)

