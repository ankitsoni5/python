def get_details(name,gender,roll,marks):
    return 'Name: ' + name +'\n Gender: ' + gender + '\n Roll: ' + str(roll) + '\n Marks: ' + str(marks)

def get_grades(marks):

    if marks >100 or marks < 0:
        print('Invalid entry.')
    elif marks >=70:
        print('A Grade.')
    elif marks >=60:
        print('B Grade.')
    elif marks >=40:
        print('C Grade.')
    else:
        print('F Grade.')
 