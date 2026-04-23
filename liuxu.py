# 以 2024 为随机数种子，随机生成 8 个在 10（含）到 100（含）之间的随机整数，每个随机数后跟随一个逗号进行分隔，屏幕输出这 8 个随机数
import random
random.seed(2024)
for i in range(8):
    print(random.randint(10,100),end=',')
# 以 888 为随机数种子，随机生成 12 个在 50（含）到 500（含）之间的随机整数，每个随机数后跟随一个逗号进行分隔，屏幕输出这 12 个随机数

random.seed(888)
for i in range(12):
    print(random.randint(50,500),end=",")








