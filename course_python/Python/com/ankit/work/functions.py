# function can take variable number of parameter for 0-n

def myadd(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum  #return (args)

# positional arguments packing 
print(myadd())
print(myadd(1))
print(myadd(1,2,3,4,5,6,7,9,54,56,654,7,8,567))


#---------------------------------------------------------

def area(lenght ,breadth):
    return lenght*breadth

stat = [6,4]
#print(area(stat[0],stat[1]))
# The order of the positonal argument matches with the order of tuple
print(area(*stat)) # pythonic way. Positional argument unpacking

#---------------------------------------------------------
# key word argument

def perimeter(**kargs):
    #print(kargs) #dict object
    return 2* (kargs['length'] + kargs['breadth']) # it will work for first case not for 2nd bcoz the key doedn't match i.e len and bre

# keyword argument packing
#print(perimeter(3,2)) # positional argument
print(perimeter(length=3, breadth=2)) # will work # key word argument
#print(perimeter(len=3, bre=2)) # will not work

#---------------------------------------------------------
# Key word argument unpacking

smap = {'breadth': 4 ,'lenght' : 5}
# print(area(smap['lenght'],smap['braedth']))
# in area function there a argument with name length and breadth  and our smap contain the same key with same name 
# so no matter of order, we can pass the argument as **smap and it work
print(area(**smap))
