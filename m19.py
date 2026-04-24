with open("n1.py", "r", encoding="utf-8") as f:
    text = f.read()
# 可以理解为，第一行对计算机说，我要"r",让计算机给我去拿来，第二行我要读取"read"计算机给我已经拿来的这本书,encoding="utf-8"写了为了防止乱码
counts = {}
#counts={}创建了一个空的字典
for char in text:

    if '\u4e00' <= char <= '\u9fff':
        #输入上面这一行是为了判断这个字符是不是中文字符
        counts[char] = counts.get(char, 0) + 1
        #出现char 就+1，没有出现就0


max_char = max(counts, key=counts.get)
#就是说counts.get是获取这个字符出现的次数，不对比
#而key=counts.get是为了对比字符出现最多次的字符
max_count = counts[max_char]

print(f"{max_char}:{max_count}")