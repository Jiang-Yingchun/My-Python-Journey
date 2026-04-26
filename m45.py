# 考生文件夹下存在一个文件 PY103.py，请写代码替换横线，不修改其他代码，实现以下功能：
# 键盘输入一段中文文本，不含标点符号和空格，命名为变量 s，采用 jieba 库对其进行分词，输出该文本中词语的平均长度，保留 1 位小数。
# 示例
# 输入：
# plaintext
# 我爱写Python程序
# 输出：
# plaintext
# 1.7
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

