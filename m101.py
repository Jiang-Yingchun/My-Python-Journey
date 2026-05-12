# 考生文件夹下存在 CSV 文件 PY301-Constellation.csv，内容示例如下：
# csv
# 序号,星座,开始月日,结束月日,Unicode
# 1,白羊座,321,419,9800
# 2,金牛座,420,520,9801
# 3,双子座,521,621,9802
# 4,巨蟹座,622,722,9803
# 5,狮子座,723,822,9804
# ...
# 其中，321 表示 3 月 21 日，419 表示 4 月 19 日，最后一列是星座符号的 Unicode 编码。

# 读取 CSV 文件中的所有星座数据；
# 接收用户输入的星座中文名称（如 “金牛座”）；
# 根据输入，输出该星座的出生日期范围，格式为 XX月XX日-XX月XX日。
# 参考输入输出示例：
# plaintext
# 请输入星座中文名称（例如，白羊座）：金牛座
# 金牛座的出生日期范围是：4月20日-5月20日
# # 导入csv模块
import csv
constellation={}
with open("m102.csv", "r", encoding="utf-8") as f:
    reader=csv.reader(f)
    for row in reader:
        name=row[1]
        start=row[2]
        end=row[3]
        constellation[name]=(start,end)
user=input()
if user in constellation:
    start_date,end_date=constellation[user]
    start_month=start_date[:-2]
    start_day=start_date[-2:]
    end_month=end_date[:-2]
    end_day=end_date[-2:]
    print(f"{user}的出生日期范围是：{start_month}月{start_day}日-{end_month}月{end_day}日")
else:
    print("输入错误。重新输入正确星座")





