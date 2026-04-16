class Student:
    def __init__(self,name,student_id):
        self.name=name
        self.student_id=student_id
        self.grades={"语文":0,"数学":0,"英语":0}

chen=Student(name="小陈",student_id="10086")
zeng=Student(name="大曾",student_id="10067")
print(chen.name)
print(zeng.grades)

