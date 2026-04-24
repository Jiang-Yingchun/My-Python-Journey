# 《命运》是著名科幻作家倪匡的作品。这里给出《命运》的一个网络版本文件，文件名为“n1.py”。
# 以
# 问题1(5分）:“n1.py”文件进行字符频次统计，输出频次最高的中文字符（不包含标点符号）及其频次，字符与频次之间采用英文冒
# 号”：“分隔，示例格式如下：
# 理:224
with open("n1.py","r",encoding="utf_8") as f:
    text =f.read()
counts={}
for char in text:
    if '\u4e00'<=char<='\u9fff':
        counts[char]=counts.get(char,0)+1
max_char=max(counts,key=counts.get)
max_count=counts[max_char]
print(f"{max_char}:{max_count}")