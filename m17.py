# 相似题目
# 键盘输入一组员工信息，每行数据包含：姓名 部门 绩效分，信息间用空格分隔，输入空行结束录入。
# 计算并输出：
# 所有员工的绩效平均分（保留 2 位小数）
# 绩效 85 分及以上的优秀员工人数
total_performance=0
count=0
performance_85=0
while True:
    info=input("输入一组员工信息，每行数据包含：姓名 部门 绩效分")
    if not info:
        break
    name,department,performance=info.split()
    performance=int(performance)
    count+=1
    total_performance+=performance
    if performance>=85:
        performance_85+=1
        avg_performance=total_performance/count
print(f"{avg_performance:.2f},{performance_85}")





