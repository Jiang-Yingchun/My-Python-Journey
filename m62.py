with open("m61.py","r",encoding="utf_8")as f:#就是encoding="utf-8"就是防止乱码用的
    lines=f.readlines()
 #lines=f.readlines()
# 就是让一个叫“lines”的东西存m61.py每一行的数据，并且每一行数据后面都会加上一个换行/n符号罢了
result=[]
#result=[]是数组的意思
in_original=True
#is_original就是一个录音开关，true就打开录音,对应的就是保留文字，false就是关掉录音，对应不保留文字
for line in lines:
    s=line.strip()
    #就是说写一个循环，for line in lines:
# s=line.strip()
# 把文件中的换行字符删掉，s 就是当前读取到的一行内容（已经去掉多余空格、换行）
    if s=="【注释】":
        in_original=False
    if in_original and s:
#     #in_original → 开关是开启状态（True）
# and s → s 不是空行（不是空白、不是只剩换行的空行）
# 合起来意思：
        result.append(s)
with open("m61.py","w",encoding="utf_8")as f:
    f.write("\n".join(result))