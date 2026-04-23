# 键盘输入一组学生的信息，每行数据包含：姓名 科目 分数，信息间用空格分隔，输入空行结束录入。
# 计算并输出：
# 所有学生的平均分（保留 2 位小数）
# 分数 90 分及以上的学生人数
total_fenshu=0
count=0
fenshu_90=0
while True:
    info=input("请输入一组学生的信息，每行数据包含：姓名 科目 分数")
    if not info:
        break
    name,subject,fenshu=info.split()
    fenshu=int(fenshu)
    count+=1
    total_fenshu += fenshu
    if fenshu>=90:
        fenshu_90 +=1
    avg_fenshu=total_fenshu/count
print(f"所有学生的平均分数{avg_fenshu:.2f},分数 90 分及以上的学生人数{fenshu_90} ")




