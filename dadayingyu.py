score =input("请输入你的分数：")
score =int(score)

if 0<=score<60:
    print("D")
elif 60<=score<70:
    print("C")
elif 70<=score<80:
    print("B")
elif 80<=score<90:
    print("A")
elif 90<=score<=100:
    print("S")
else:
    print("请重新输入0~100之间的数字")
    
    
    
