with open("m64.py","r",encoding="utf-8") as f:
    lines=f.readlines()#就是让lines存m54.py的每一行数据
result=[]
is_original=True
for line in lines:
    s=line.strip()
    if s=="【注释】":
        is_original=False
    if is_original and s:
        result.append(s)
with open("m64.py","w",encoding="utf-8") as f:
    f.write("\n".join(result))