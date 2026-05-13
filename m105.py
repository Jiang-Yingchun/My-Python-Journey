import random
random.seed(0)
res=0
for i in range(5):
    num=random.randint(1,97)
    res+=num**2
print(res)