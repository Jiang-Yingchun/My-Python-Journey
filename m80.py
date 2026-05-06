data=[]
while True:
    line=input()
    if not line.strip():
        break
    name,money=line.split()
    data.append((name,int(money)))
max_info=max(data,key=lambda s:s[1])
min_info=min(data,key=lambda x:x[1])
avg=sum(m[1] for m in data)/len(data)
print(f"{max_info[0]}{max_info[1]},{min_info[0]}{min_info[1]},{avg:.2f}")