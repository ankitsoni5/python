path="D:\\ankit.txt" # also use "D:/ankit.txt"

ft = open(path) # by default mode is 'rt'
print(ft)
print(type(ft))

# reading file and printing content
print('reading for the first time.')
for line in ft:
    #print(line)
    print(line.rstrip()) # rstrip is used to remove the \n.

print('----------------------------')
print('reading for the second time.')
for line in ft:
    #print(line)
    print(line.rstrip()) # rstrip is used to remove the \n.

# reading from the file is pointer sensitive. 
# The previous read operation will got the file pointer to EOF.
# For reading it again reset the pointer.

ft.seek(0) # reset the pointer
print('----------------------------')
print('reading for the third time.')
for line in ft:
    print(line.rstrip()) # rstrip is used to remove the \n.

ft.seek(0)
# read all the lines in one shot.
print('----------------------------')
print('reading for the forth time.')
lines = ft.readlines()
print(lines)
print(type(lines))

# read all contents in a shot in str format.
ft.seek(0)
print('----------------------------')
print('reading for the fifth time.')
lines1 = ft.read()
print(lines1)
print(type(lines1))

ft.seek(0)

# close the connection to file resource once done.
ft.close() # always close it.