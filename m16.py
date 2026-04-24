# 键盘输入一组学生的信息，每行数据包含：姓名 科目 分数，信息间用空格分隔，输入空行结束录入。
# 计算并输出：
# 所有学生的平均分（保留 2 位小数）
# 分数 90 分及以上的学生人数
total_grade=0
count=0
grade_90=0
while True:
    info=input("请输入一组学生的信息，每行数据包含：姓名 科目 分数")
    if not info:
        break
    name,subject,grade=info.split()
    grade=int(grade)
    count+=1
    total_grade+=grade
    if grade>=90:
        grade_90 += 1
    avg_grade=total_grade/count
print(f"所有学生的平均分:{avg_grade:.2f},分数 90 分及以上的学生人数:{grade_90}")

