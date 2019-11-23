# Dictionary
d= {}
print(type(d))

di = {10:('Ankit', 20), 20: ('Soni', 30)}
print(type(d))
print(di) 
# value can be any python object
# key has to be immutable pyton object
# the key can't be a list and set object
# Key should be unique
# It ia a mutable data structure

di[30] = ('Anjani', 90)  #di[key] addition
di[10] = ('Anki', 50)  #di[key]  updating (Syntext is same of update and add)

di.keys() # get all the keys
'''
for key in di.keys():
    print(key)

# give the keys only
'''
di.values() # give values of all keys

#di[50] # give value of key 50

# print the name and roll no from the dictionary 
dict1 = {10:('Ankit', 20), 20: ('Soni', 30), 30: ('Anjani', 90)}

'''for key in dict1:
    print('Name : ' + dict1[key][0])
    print('Roll No :' + str(key))
    print('-----------------------')
'''
print('==========================')
v1 = dict1.items() # give the list of all the dict data in form of tuple
for k,v in v1:
    print('Name: ' + v[0])
    print('Roll No: ' + str(k))
    print('-------------------')