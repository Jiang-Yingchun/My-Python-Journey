# 某商店出售某品牌运动鞋，每双定价160，1双不打折，2双（含）到4双（含）打九折，5双（含）到9双（含）打八折，10双（含）以上打七折，键盘输入购买数量，屏幕输出总额（保留整
# 数)。示例格式如下：
# b
# 输入：1
# 输出：总额为：160
quantity=int(input("请输入你买的运动鞋的数量,请输入大于0的数量"))
if quantity==1:
    print(160)
elif quantity>=2 & quantity<=4:
    print(160*0.9*quantity)
elif quantity>=5 & quantity<=9:
    print(16*0.8*quantity)
else:
    print(160*0.7*quantity)
