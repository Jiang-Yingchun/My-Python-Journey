# 相似题 1
s=input()
words=jieba.lcut(s)
words_reversed=words[::-1]#：：这个是字符串全取一遍，如果你你只写了:，比如1:3那么输出的是，喜欢， 吃
print(','.join(words_reversed))


# 题目：键盘输入一句话，用 jieba 分词后，将切分的词组按原顺序的逆序输出，词组之间用逗号分隔。
# 示例：
# 输入：我喜欢吃苹果
# 输出：苹果,吃,喜欢,我
import jieba
