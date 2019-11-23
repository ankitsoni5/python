from com.ankit.college.student import Student
from com.ankit.college.professor import Professor

s = Student(name='Ankit',gender='M',roll=1,marks=100)
p = Professor(name='Anjani',gender='F',subjects=['Physics','Chemistry','Maths'])

i = 10

print(i)
# internally: print(i.__str__())
# python: print(int.__str__(i)) 
print(s)
# internally: print(s.__str__())
# python: Student(int.__str__(s))
print(p)
# internally: print(p.__str__())
# python: Professor(int.__str__(p))
'''print(s.name)
print(s.gender)
print(p.name)
print(p.subjects)
'''
#Overriden methon will be called over parent class in student.
print(s.get_details())
print(p.get_details())