# 45、考生文件夹下存在一个文件 PY202.py，该文件是本题目的代码提示框架，其中代码可以任意修改。请在该文件中编写代码，以实现如下功能:
# 键盘输入一组我国高校所对应的学校类型，以空格分隔，共一行，示例格式如下:
# 理工 综合 综合 综合 师范 理工
# 统计各类型的数量，从数量多到少的顺序屏幕输出类型及对应数量，以英文冒号分隔，每个类型一行，输出参考格式如下:
# 综合：3
# 理工：2
# 师范：1
n=input("键盘输入一组我国高校所对应的学校类型").split()
count={}
for i  in n:
    count[i]=count.get(i,0)+1
items=list(count.items())
items.sort(key=lambda x:x[1],reverse=True)
for subject,num in items:
    print(f"{subject}: {num}")