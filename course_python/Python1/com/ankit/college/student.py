# is-a-test: Student IS-A College user
# Student become sub class
# inheritance

from .collegeuser import Collegeuser # . means current directly of the module

class Student(Collegeuser):
    def __init__(self,name,gender,roll,marks):
        super().__init__(name,gender)
        #internally
        #Collegeuser.__init__(self, name, gender)
        self.roll = roll
        self.marks = marks
    
    # Over-rided method of parent class for getting all the data of student
    def get_details(self):
        p1 = super().get_details() # calls the suprclass method even inspite of overriden method
        p2='\nRoll: {0}\nMarks: {1}'.format(self.roll,self.marks)
        return p1+p2