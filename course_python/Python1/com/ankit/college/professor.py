# IS-A-relation : Professor IS-A college user

from .collegeuser import Collegeuser

class Professor(Collegeuser):
        def __init__(self,name,gender,subjects):
                super().__init__(name,gender)
                #internally
                #Collegeuser.__init__(self, name, gender)
                self.subjects = subjects