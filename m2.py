# 键盘输入一组学生的姓名、班级、成绩，信息间空格分隔，每人一行，空行结束录入。
# 计算输出：平均成绩（保留 2 位小数）、90 分及以上的人数。
# 输入示例
# 小明 1 班 88
# 小红 2 班 95
# 小刚 1 班 92
total_grades=0
grade_90=0
count=0
while True:
    info=input("请输入一组学生的姓名、班级、成绩")
    if not info:
        break
    name,class_number,grade=info.split()
    grade=int(grade)
    total_grades+=grade
    count+=1
    if grade>=90:
        grade_90+=1
avg_grade=total_grades/count
print(f"平均成绩是{avg_grade:.2f} 90分以上的人数是{grade_90}")



