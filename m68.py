with open("m67.py","r",encoding="utf-8") as f:
    lines=f.readlines()
result=[]
is_original=True
for line in lines:
    s=line.strip()
    if s=="【注释】":
        is_original=False
    if is_original and s:
        result.append(s)
with open("m67.py","w",encoding="utf-8") as f:
    f.write("n/".join(result))


