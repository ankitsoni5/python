# Every class in Python implicitly extend Object Class

class Collegeuser:
    def __init__(self,name,gender):
        # self - Student, Professor (any sub class object)
        self.name = name
        self.gender = gender

    def get_details(self):
        return 'Name: {0}\nGender: {1}'.format(self.name,self.gender)

    def __str__(self):
        return 'Name: {0}\nGender: {1}'.format(self.name,self.gender)
    

    