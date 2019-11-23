from csv import reader,writer
from shutil import copy2

path = "D:\\ankit\\ankit.csv"
des_path = "D:\\ankit.csv"

'''
# only to read a csv file file get data and manipulate it.
with open(path) as fs:
    csv_reader = reader(fs)
    for row in csv_reader:
        #print(row) # list of token for the csv file
        name, marks = row[0],  row[1]
        print(name)
        print(marks)
        #till here we have extracted the data and used it.

'''
# perform operation on csv and extract some data in other csv file
# here we are reading data of a csv file, picking out name and marks, 
# calculating grades and writing it into an other csv file
def grades(n):
    if n >100 or n < 0:
        return 'Invalid entry.'
    elif n >=70:
        return 'A-Grade.'
    elif n >=60:
        return 'B-Grade.'
    elif n >=40:
        return 'C-Grade.'
    else:
        return 'F-Grade.'

with open(path) as fs:
    csv_reader = reader(fs)
    with open(des_path,mode='wt') as fd:
        csv_writer = writer(fd)
        for row in csv_reader:
            #print(row) # list of token for the csv file
            name, marks = row[0],  row[1]
            g1 = grades(int(marks))
            #print(name,g1)
            csv_writer.writerow([name,g1])

