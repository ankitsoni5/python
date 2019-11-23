''' 
# list is mutable
# Dupliates are allowed
# maintain order i.e. it is ordered data structure

# e1 = [] empty list
# e2 = [0, 1, 2, 3, 4]
# list can create homogenoue and hetrogeneus elements (data types)
  e3 = ['Ankit', 'M', 22, 90]

# list.append([20]) (to append single value)
  list .extend([30.40]) (to append multiple value)
  list.insert(1, 'soni') (insert at particular location)
# list.pop() to remove the element from last
  list.pop([3]) remove the element from that index

# list.reverse() > reverse the list
# list.sort() > sort in ascending
  list.sort(reverse=True) > for decending

# list.clear() > to clear the list
# list.copy()  > to create the copy

# '|' join list > it will give you a new String with | saperated values of list

# list.split(' ') > Split the values saperated by ' '
'''
pointers = [5, 10, 8, 4, 6, 7, 11, 3, 2]
#new_odd_pointer=[]
#new_even_pointers=[]

# bring out odd and even pointers in new list
'''for n in pointers:
    if n%2:
        new_odd_pointer.append(n)
    else:
        new_even_pointers.append(n)

print('Odd Pointers: ' + str(new_odd_pointer))
print('Even Pointers: ' + str(new_even_pointers))
'''
#using for comprihention
# pre-requiste: you require new list
odds = [pointer for pointer in pointers if pointer % 2] #only if condition is true then only pointer will be added
print(odds)

# create a list with even list greater then 5
even = [pointer for pointer in pointers if not pointer % 2 and pointer > 5]
print(even)

# get new list of pointers decucted by one (mapping method)
deduct = [pointer -1 for pointer in pointers]
print(deduct)

# get a new list of square of all odd pointers greater than or equal to 5 from pointers list
square = [(pointer**2) for pointer in pointers if pointer % 2 and pointer >= 5]
print(square)