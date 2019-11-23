from com.ankit.collage.student import Student
'''
# It is using list.

slist = [
    Student(name='Ankit', gender='M', roll=1, marks=90),
    Student(name='Soni', gender='M', roll=2, marks=80),
    Student(name='Anjani', gender='F', roll=3, marks=70)
]

roll_no = int(input('Enter the roll number: '))
#student_found = False
for s in slist:
    if roll_no == s.roll:
        print(Student.getdetails(s))
        #student_found=True
        break
else:
    # execute when the 'for' loop ran completely and result not found then for we have else block for this. 
    print('Student not found')

#if not student_found:
    print('Student not found')
#
'''
# It is using list.
dlist = {
    1: Student(name='Ankit', gender='M', roll=1, marks=90),
    2: Student(name='Soni', gender='M', roll=2, marks=80),
    3: Student(name='Anjani', gender='F', roll=3, marks=70)
}
roll_no_1 = int(input('Enter the roll number: '))
if roll_no_1 in dlist:
    student = dlist[roll_no_1]
    print(student.getdetails())
else:
    print('Student not found.')