# 题目 2
# 输入整数 n，取出 chr(n) 前 1 个、后 2 个字符拼接，整体宽度 18、&填充、右对齐。
n=int(input())
s=chr(n-1)+chr(n)+chr(n+1)
print(f"{s:&>18}")