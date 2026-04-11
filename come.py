list=["你","好","吗","我","是","李","蕾"]
for char in list:
    print(char)
list1=["你","好","吗","我","是","李","蕾"]
for i in range(len(list1)):
    print(list1[i])
list2=["你","好","吗","我","是","李","蕾"]
i = 0
while i <len(list2):
    print(list2[i])
    i=i+1
    #我是分割线------------------------------------------------------------------------------------------
print("我是一个求平均数的程序")
total = 0
count = 0
user_input = input("请输入数字，完成所有数字之后请输入q终止程序")
while user_input !="q":
    num = float(user_input)
    total +=num
    count +=1
    user_input =input("请输入数字，完成所有数字之后请输入q终止程序")
if count==0:
    result=0
    #写这一条是因为被除数不能为零
else:
    result=total/count
print("您输入的数字平均值为"+str(result))



