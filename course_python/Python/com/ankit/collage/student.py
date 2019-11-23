'''
> for every class in python, a memory (object) is allocated for it.
> 1 object per class 
'''
class Student:

    count = 0 #class attribute (It is by default static, we don't have to give static. there is nothing like static variable in python)
    # access: className.classAttribute

    def __init__(self,name='Default',gender='Default',roll=0,marks=0):
        # only related to creating the attribute in an object.
        # Constructor : invoked when the class is invoked.
        # always reture 'self' by itself.
        self.name = name
        self.gender = gender # These are object attribute
        self.roll = roll
        self.marks = marks

        Student.count +=1

    # Object function, as it is taking self as a input
    def getdetails(self):
        # self means current object
        #return 'Name: ' + self.name +'\n Gender: ' + self.gender + '\n Roll: ' + str(self.roll) + '\n Marks: ' + str(self.marks)
        return 'Name: {0}\nGender: {1}\nRoll: {2}\nMarks: {3}'.format(self.name,self.gender,self.roll,self.marks) #can be done in both ways
        #return 'Name: {name}\nGender: {gender}\nRoll: {roll}\nMarks: {marks}'.format(name=self.name,gender=self.gender,roll=self.roll,marks=self.marks)

    def get_grades(self):
        if self.marks >100 or self.marks < 0:
            return 'Invalid entry.'
        elif self.marks >=70:
            return 'A Grade.'
        elif self.marks >=60:
            return 'B Grade.'
        elif self.marks >=40:
            return 'C Grade.'
        else:
            return 'F Grade.'

    # These are class funtions, as it doesn't using object attribute
    # access: classname.classfunction
    def get_min_attendence():
        # code to fetch is the common min attendance criteria for students
        return 70

    def get_name_and_roll(self):
        return (self.name, self.roll) # it will return tuple as it is returned in ()