n=int(input("请输入一个正整数n:"))
while n>=1:

    if n%23==0:
        print(n)
        break
    n-=1
else:
    print("没找到")
