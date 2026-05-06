# 键盘输入多名学生的姓名及每月生活费，信息间采用空格分隔，每个学生一行，空行回车结束录入，示例格式如下：
# plaintext
# 张三 1500
# 李四 1800
# 王五 1200
# 赵六 2000
# 屏幕输出生活费最高的学生及金额，生活费最低的学生及金额，以及平均生活费（保留 2 位小数）。
# 输出格式示例：
# 生活费最高的学生是赵六 2000,生活费最低的学生是王五 1200,平均生活费是1625.00
data=[]
while True:
    line=input()
    if not line.strip():
        break
    name,money=line.split()
    data.append((name,int(money)))
max_info=max(data,key=lambda x:x[1])
min_info=min(data,key=lambda x:x[1])
avg=sum(m[1] for m in data)/len(data)
print(f"{max_info[0]}{max_info[1]},{min_info[0]}{min_info[1]},{avg:.2f}")









