# 键盘输入一组员工的姓名、部门、工龄，信息间空格分隔，每人一行，空行结束录入。
# 计算输出：平均工龄（保留 2 位小数）、工龄 5 年及以上的人数。
# 输入示例
# 赵六 技术 3
# 钱七 运营 6
# 孙八 技术 8
total_working_years=0
count=0
working_years_5=0
average_working_years=0
while True:

    info=input("键盘输入一组员工的姓名、部门、工龄")
    if not info:
        break
    name,department,working_years=info.split()
    working_years=int(working_years)
    count+=1
    total_working_years+=working_years
    if working_years>=5:
        working_years_5+=1

    average_working_years=total_working_years/count
print(f"平均工龄{average_working_years:.2f} 工龄 5 年及以上的人数{working_years_5}")


