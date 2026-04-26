# 2、考生文件夹下存在一个文件PY102.py，请写代码替换横线，不修改其他代码，实现以下功能：
# 键盘输入一段中文文本，不含标点符号和空格，命名为变量s，采用jieba库对其进行分词，输出该文本中词语的平均长度，保留1位小数。
# 例如：键盘输入：吃葡萄不吐葡萄皮
# 屏幕输出：1.6
import jieba
s=input()
words=jieba.lcut(s)
count=0
total_word=0
for word in words:
    total_word+=len(word)
    count+=1
avg_word=total_word/count
print(f"{avg_word:.1f}")