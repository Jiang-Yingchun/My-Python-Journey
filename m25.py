# 、用python编写程序“1-2+3-4+5-6+7…..-100”并输出结果 。
res=0
for i in range(1,101):
    if i %2!=0:
        res=res+i
    else:
        res=res-i
    
print(res)




