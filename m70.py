# 任务 1
# 提取所有原文（去掉【注释】、空行、多余空格），保存为：
# m69.py
# 要求：保留 (1)(2) 这类标注，无空行。
with open("m69.py","r",encoding="utf-8") as f:
    lines=f.readlines()
result=[]
is_original=True
for line in lines:
    s=line.strip()
    if s=="【注释】":
        is_original=False
    if is_original and s:
        result.append(s)
with open("m69.py","w",encoding="utf-8") as f:
    f.write("n/".join(result))



