# 键盘输入某班各个同学就业的行业名称，行业名称之间用空格间隔（回车结束输入）。完善Python代码，统计各行业就业的学生数量，按数量从高到低方式输出。例如输入：
# 交通金融计算机交通计算机计算机
# 输出参考格式如下，其中冒号为英文冒号：
# 计算机:3
# 交通:2
# 金融:1
names=input("请输入各个同学行业名称，行业名称之间用空格间隔（回车结束输入）")
industry_list =names.split()
d={}
for industry in industry_list:
    if industry in d:
        d[industry]+=1
    else:
        d[industry]=1
ls=list(d.items())
ls.sort(key=lambda x:x[1],reverse=True)
for k in ls:
    print("{}:{}".format(k[0],k[1]))