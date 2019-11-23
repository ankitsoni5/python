# list is mutable, tuple is immutable 
# it is ordered
# it is good for storing hetrogeneus data as it is immutable.
# 

sd = ('Ankit', 'M', 22, 90)
print(type(sd))
print(sd)
print(sd[0],sd[1]) # indexing
print(sd[0:2]) # slicing
print(sd[-3:])

sc = ('Ankit') # here it will create a str object bcoz bracket is here consider for precidence

# to create single element for tuple
single = ('Ankit',)
print(type(single))
print(single)

# blank tuple
blank = ()
print(type(single))
print(blank)


# data conversion from list to tuple and vise-versa
tt = (1,2,3,4,5,6,7)
print(tt)
l = list(tt)
print(l)
t1 = tuple(l)
print(tt)