import re
with open("m71.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

result = []
for line in lines:

    new_line = re.sub(r"\(\d+\)", "", line.strip())
    #上一行的这个代码，先用叫new_line的东西存起来
    #套用一个公式：re.sub(要找的东西，要替换成的内容，去掉/n以及行首和行尾的空白的原字符串）
    result.append(new_line)

with open("m71.py", "w", encoding="utf-8") as f:
    f.write("\n".join(result))