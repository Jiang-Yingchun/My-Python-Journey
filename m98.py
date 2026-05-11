# 45、考生文件夹下存在一个文件PY202.py，该文件是本题目的代码提示框架，其中代码可以任意修改。请在该文件中编写代码，以实现如下功能：
# 键盘输入小明学习的课程名称及考分等信息，信息间采用空格分隔，每个课程一行，空行回车结束录入，示例格式如下：
# 数学 90
# 语文95
# 英语86
# 物理84
# 生物 87
# 屏幕输出得分最高的课程及成绩，得分最低的课程及成绩，以及平均分（保留2位小数）。
# 注意，其中逗号为英文逗号，格式如下：
# 最高分课程是语文95，最低分课程是物理84，平均分是88.40
data=[]
while True:
    line=input()
    if not line.strip():
        break
    subject,grade=line.split()
    data.append((subject,int(grade)))
max_info=max(data,key=lambda x:x[1])
min_info=min(data,key=lambda x:x[1])
avg=sum(m[1] for m in data)/len(data)
print(f"最高分课程是{max_info[0]}{max_info[1]},最低分课程是{min_info[0]}{min_info[1]},平均分是{avg:.2f}")
# line.strip()判断是不是空行，line.split()分割字符，data这个玩意里面的数据最全，所以写max_info=max(data,key=lambda x:x[1]), 不能写Line是因为line里面的数据是临时的 ，例如如果你输入 语文 85
# 数学 94,
# 最后line只看最新的 ，只能输出给你数学 94


