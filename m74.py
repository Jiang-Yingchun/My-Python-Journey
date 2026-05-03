import re
with open("m72.py","r",encoding="utf-8")as f:
    lines=f.readlines()
result=[]
for line in lines:
    new_lines=re.sub(r"\(\d+\)","",line.strip())
    #上一行的r就是给计算机当翻译的，告诉计算机这是\，她的意思是\是转义字符，而如果没有r，没有r,计算机读取\n(\d+\)会大概率直接报错
    result.append(new_lines)
with open("m72.py", "w", encoding="utf-8") as f:
    f.write("\n".join(result))
