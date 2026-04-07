print("我知道了，你今年"+str(2)+"岁了！")
#把整数爆改字符串
sister_age=int(input("请输入你妹妹的年龄"))
future_sister_age=sister_age + 10
print("你妹妹十年后的年龄为",future_sister_age)
user_age=input("请输入您的年龄")

print("OK，我知道了您的年龄几年是",user_age,"岁")
mu=input("请输入的心理满足值")
print("ok,我知道了你的Mu是："+mu)
weight=float(input("请输入你的体重（单位：kg）:"))
height=float(input("请输入你的身高（单位：米）"))
BMI=weight/height**2
print("你的BMI值为：",BMI)
#偏瘦:user_BMI<= 18.5  #正常:18.5 < user_BMI<= 25    #偏胖:25< user_BMI <= 30       #肥胖:user_BMI>30
if BMI<=18.5:
    print("您的体脂率偏瘦")
elif 18.5<BMI<=25:
    print("您的体脂率正常")
elif 25<BMI<=30:
    print("您的体脂率偏胖")
else:
    print("您的体脂率肥胖")


grade=int(input("你这次考试的分数多少？"))
if grade>=60:
    print("你妈妈允许你买电脑")
else:
    print("你妈妈不允许你买电脑")
