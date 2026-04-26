import jieba

# 1. 输入文本（可以去掉提示文字，也可以保留，题目不限制）
s = input()

# 2. 分词：把jcut改成正确的lcut
words = jieba.lcut(s)
# 就是说words=jieba.lcut(s)中jieba 是刀的名字，然后用这把刀cut,切成一个个列表list，用words存起来


total_len = 0
word_count = 0

for word in words:
    # 这里要+=，不是=，否则会覆盖前面的长度
    total_len += len(word)
    word_count += 1

avg_len = total_len / word_count

# 3. 格式化输出，保留1位小数
print(f"{avg_len:.1f}")
