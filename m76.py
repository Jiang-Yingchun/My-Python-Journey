# 📝 练习题
# 题目：
# 键盘输入一个英文句子（不含标点），按空格分词后，将每个单词按原顺序的逆序输出，单词之间用空格分隔。
# 示例：
# 输入：I love learning Python
# 输出：Python learning love I
import jieba
s=input()
word=jieba.lcut(s)
words=word[::-1]
print(' '.join(words))
