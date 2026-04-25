# 输入一行字符，分别
# 统计出其中英文字母、空格、数字和其
# 它字符的个数
s=input("请输入一列字符串")
char=0
space=0
digit=0
others=0
for c in s:
    if c.isalpha():
        char+=1
    elif c.isdigit():
        digit+=1
    elif c.isspace():
        space+=1
    else:
        others+=1
print(f"char={char},space={space},digit={digit},others={others}")
#（）是方法名，而方法名执行要加（）
