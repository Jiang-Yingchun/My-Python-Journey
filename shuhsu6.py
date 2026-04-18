goods=[]
for i in range(5):
    price=int(input(f"请输入第{i+1}件商品的价格"))
    goods.append(price)
sum_price=sum(goods)#直接用sum()求列表总和
sum_tax=sum_price*0.07
pay=sum_price+sum_tax
print(f"消费总额为：{sum_price}")
print(f"消费税为：{sum_tax:.2f}")
print(f"应付款为{pay}")
#总而言之，如果你想打印出{}里面的数字，就在"”最前面加一个f
#此外，如果你想保留两位小数就在}前面写:.2f
#:.2f
# sum_price=goods[0]+goods[1]+goods[2]+goods[3]+goods[4]
# print("消费总额为",sum_price)
# sum_tax=(goods[0]+goods[1]+goods[2]+goods[3]+goods[4])*0.07
# print("消费税为",sum_tax)
# pay=sum_price+sum_tax
# print("应付款为",pay)