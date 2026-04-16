class Student:
    def __init__(self,name,student_id):
        self.name=name
        self.student_id=student_id
        self.grades={"语文":0,"数学":0,"英语":0}
    def set_grade(self,course,grade):
        if course in self.grades:
            self.grades[course]=grade
    def print_grades(self):
        print(f"学生{self.name}(学号：{self.student_id}）的成绩为:")
        for course in self.grades:
            print(f"{course}:{self.grades[course]}分")


chen=Student(name="小陈",student_id="1234567")
# zeng=Student(name="小曾",student_id="12345678")
chen.set_grade("语文",87)
chen.set_grade("数学",94)
chen.print_grades()
# print(zeng.name)
# chen.set_grade("数学",95)
# print(chen.grades)