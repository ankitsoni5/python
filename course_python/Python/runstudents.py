from com.ankit.utilities.student_ops import get_details,get_grades

name = input('Enter name: ')
gender = input('Enter gender: ')
roll = int(input('Enter roll: '))
marks = float(input('Enter marks: '))

print(get_details(name,gender,roll,marks))
get_grades(marks)