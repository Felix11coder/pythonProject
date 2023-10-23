class student:
    def __init__(self,name,course,gender,age):
        self.name=name
        self.course=course
        self.gender=gender
        self.age=age
    def wanafunzi(self):
        print("Name: %s \nCourse: %s\nGender: %s\nAge: %d\n"
              %(self.name, self.course, self.gender, self.age))

stud1=student("Felix KImani", "Applied computer Science", "Male", 22)
stud1.wanafunzi()

stud2=student("Eric Were", "Computer Science", "Male", 30)
stud2.wanafunzi()

stud3=student("Naomi Wanja", "Food technology", "Female", 20)
stud3.wanafunzi()

stud4=student("Cate Nasieku", "ELectrical Engineering", "Female", 21)
stud4.wanafunzi()