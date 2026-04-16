class Student:
    def __init__(self,name,student_id):
        self.name=name
        self.student_id=student_id
        self.grades={"数学":0,"语文":0,"英语":0}
    def set_grade(self,course,grade):
        for course in self.grades:
            self.grades[course]=grade
    def print_grade(self):
        print(f"学生的名字为：{self.name}，学号为{self.student_id},这位学生的成绩为")
        for course in self.grades:
            print(f"{course}是{self.grades[course]}")

chen=Student(name="小陈",student_id="234567")
chen.set_grade(course="数学",grade=90)
chen.set_grade(course="语文",grade=90)
chen.print_grade()
