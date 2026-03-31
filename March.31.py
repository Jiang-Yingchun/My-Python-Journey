"""小游戏"""
import random
counts =3
answer =random.randint(1,19)
while(counts>=0):
    shuzi=input("请输入一个数字")
    guess=int(shuzi)
    if guess==answer:
        print("猜对了")
        break
    else:
        if guess<answer:
            print("猜小了")
        else:
            print("猜大了")
    counts=counts-1
print("游戏结束!")
