# 替换横线，不修改其他代码，实现以下功能：
# 键盘输入一句话，用jieba分词后，将切分的词组按照在原话中逆序输出到屏幕上，词组中间没有空格。示例如下：
# 输入：
# 我爱妈妈
# 输出：
# 妈妈爱我
import jieba
s=input()
word=jieba.lcut(s)
words=word[::-1]
print("".join(words))