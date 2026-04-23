# 键盘输入一组人员的姓名、性别、年龄等信息，信息间采用空格分隔，每人一行，空行回车结束录入，示例格式如下:
# 张三 男 23
# 李四 女 21
# 王五 男 18
# 计算并输出这组人员的平均年龄 (保留 2 位小数) 和其中男性人数，格式如下:
# 平均年龄是 20.67 男性人数是 2
total_age=0
male_count=0
count=0
while True:
    info =input()
    if not info:
        break
    name,gender,age=info.split()
    age=int(age)
    total_age+=age
    count+=1
    if gender=="男":
        male_count+=1
avg_age=total_age/count
print(f"平均年龄是{avg_age:.2f} 男性人数是{male_count}")


