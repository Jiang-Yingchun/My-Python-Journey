r=float(input("请输入一个半径"))
print("该半径的圆的周长为",2*3.14*r)
print("该半径的圆的面积为",3.14*r**2)
print("有该半径的球体的表面积",4*3.14*r**2)
print("有该半径的球体的体积",4/3*3.14*r**3)
list=["1","2","3","4","5","上","山","打老虎"]
for i in list:
    print(list)
list1=["2","2","3","4","5","上","山","打老虎"]
for n in range(len(list1)):
    print(list1[n])
list2=["3","2","3","4","5","上","山","打老虎"]
g=0
while g <len(list2):
    print(list2[g])
    g=g+1
    #我是分割线
print("你好，欢迎；来到输入数字，给你平均数的游戏")
total=0
count=0
user_input=input("请输入一个数字，停止时，请输入小写字母q")
#因为有字母q，所以一上来就不能写int(input("请输入一个数字，停止时，请输入小写字母q"))
while user_input !="q":
    num=float(user_input)#确定不是字母q之后才能转为浮点数，然后这个浮点数我们叫他num
    total+=num
    count+=1#count是为了之后除以个数用到的
    user_input = input("请输入一个数字，停止时，请输入小写字母q")#为了继续读取用户键盘上的数字或者q写的代码

if count==0:
    result=0
    print(result)
else:
    result=total/count
    print(result)


