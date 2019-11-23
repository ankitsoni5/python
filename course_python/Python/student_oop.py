from com.ankit.collage.student import Student

#s1 = Student() #student object
#internally
# 1. get address - 4001 Student Object
# 2. Student : __init__(4001)
print(Student.count) # it will give the number of count of object created of Student class.

s1 = Student('Abhishek', 'Male', 1, 90)
#internally
# 1. get address - 4001 Student Object
# 2. Student : __init__(4001,'Abhishek', 'Male', 1, 90)

# create an attribute in an object
'''s1.name = 'Ankit'
s1.gender = 'M'
s1.roll = 21
s1.marks = 80

s2 = Student() # 2nd student object
s2.name = 'Soni'
s2.gender = 'M'
s2.roll = 22
s2.marks = 54
'''
print(Student.count)

s2 = Student('Soni','M',22,54) # 2nd student object
print(s1.getdetails())
print(s1.get_grades())
print(s1.get_name_and_roll()) #using tuple as a return data.
tu = s1.get_name_and_roll()
name, roll = tu[0],tu[1]    # getting saterate values from returen value
# internally
#print(Student.getdetails(s1))
print(s2.getdetails())
print(s2.get_grades())
print(Student.count)

s3 = Student() # to run this also make the __init__ method with default arguments so that if you don't pass any arg it will take default values
print(s3.getdetails())
print(s3.get_grades())

print(Student.count)

print(Student.get_min_attendence())
