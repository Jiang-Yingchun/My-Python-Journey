# 45、考生文件夹下存在一个文件PY202.py，请在该文件中作答，实现以下功能。
# 键盘输入某班各个同学就业的行业名称，行业名称之间用空格间隔（回车结束输入）。完善Python代码，统计各行业就业的学生数量，按数量从高到低方式输出。例如输入：
#交通 金融 计算机 交通 计算机 计算机
# 输出参考格式如下，其中冒号为英文冒号：
# 计算机:3
# 交通:2
# 金融:1
# 提示：建议使用本机提供的Python集成开发环境IDLE编写、调试及验证程序。
industries=input("输入某班各个同学就业的行业名称").split()
counts={}
for i in industries:
   counts[i]=counts.get(i,0)+1

items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for industry,num in items:
    print(f"{industry}: {num}")
