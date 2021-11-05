import random


def get_color(number):
    # making sure is a number and not a string
    color_number = int(number)

    switcher={
                  0:'red',
                  1:'yellow',
                  2:'blue',
                  3:'green',
                  4:'black'
              }
    return switcher.get(number,"Invalid Color Number")


def get_allStudentColors():
    
    students_array = []
    for i in range(10):
        random_number = random.randint(0,4)
        result = get_color(random_number)
        students_array.append(result)
    
    return students_array





print(get_allStudentColors())