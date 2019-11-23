# Set data Structure (SDS)
# It does not allow duplicate
# No order is maintained
# It is mutable
# No concept of indexing and Slicingas there is no order
# fruits = {'apple', 'grapes'}
# can't create empty set

fruits = {'apple', 'grapes'}
print(type(fruits))

empty = []
tp = set(empty)
print(tp)


# performing set operations
m1 = [1, 3, 5, 10]
m2 = [3, 4, 5, 9]

s1 = set(m1)
s2 = set(m2)

'''common = []
for a in m1:
    if a in m2:
        common.append(a)
'''
print(s1 & s2) # intersection
print(s1 - s2) # in s1 only (s1 not in s2)
print(s2 - s1) # in s2 only
print(s1 | s2) # union
print(s1 ^ s2) # all except intersection

# unique set of pointers in the class
pointers = [10, 6, 5, 3, 6, 9, 10, 1, 3, 4, 10, 5]
unique = set(pointers)
list_unique = list(unique)
print(list_unique)
