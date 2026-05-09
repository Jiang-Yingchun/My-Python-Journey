import math
for i in range(500,1000):
    is_prime=True
    j=2
    while j*j<=i:
        if i%j==0:
            is_prime=False
            break
        j+=1
    if is_prime:
        print(i)
        break
