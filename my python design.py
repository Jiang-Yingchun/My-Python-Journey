""""用python设计的猜数字小游戏"""
counts=3
while(counts>=0):
    shuzi=input("请输入一个数字，看你想的跟我一样不一样")
    guess=int(shuzi)

    if guess==55:
        print("恭喜你猜对啦！")
    else:
        if guess<55:
            print("猜小了")
        else:
            print("猜大了")
    counts=counts-1
print("游戏结束")
