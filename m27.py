s=input("请输入一个字符")
char=0
space=0
digit=0
others=0
for c in s:
    if c.isalpha():
        char+=1
    elif c.isspace():
        space+=1
    elif c.isdigit():
        digit+=1
    else:
        others +=1
print(f"char={char},space={space},digit={digit},others={others}")


