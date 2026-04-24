i=2
while i<=100:
    j=2
    flag=True
    while j*j<i:
        if i%j==0:
            flag=False
            break
        j+=1
    if flag:
        print(i,end=" ")#end=" "是空格的意思
    i+=1

