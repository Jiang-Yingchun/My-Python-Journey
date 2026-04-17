class Student:
    def __init__(self,name,student_id):
        self.name=name
        self.student_id=student_id
        self.grades={"数学":0,"语文":0,"英语":0}
    def set_grades(self,course,grade):
        if course in self.grades:
            self.grades[course]=grade
    def print_grade(self):
        print(f"学生的名字为{self.name},学号为{self.student_id}，成绩为:")
        for course in self.grades:
            print(f"{course}是{self.grades[course]}")
chen=Student(name="小陈",student_id="1234567")
chen.set_grades(course="数学",grade="90")
chen.set_grades(course="英语",grade="89")
chen.print_grade()



