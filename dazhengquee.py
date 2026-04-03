Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:01:40) [MSC v.1944 32 bit (Intel)] on win32
Enter "help" below or click "Help" above for more information.
i=0
while i<=5:
    print("内循环为",i)
else:
    print("外循环为",i)

    
内循环为 0
内循环为 0
内循环为 0
内循环为 0
内循环为 0
内循环为 0
内循环为 0
内循环为 0
内循环为 0
内循环为 0
内循环为 0
内循环为 0
内循环为 0
内循环为 0
内循环为 0
内循环为 0
内循环为 0
内循环为 0
内循环为 0
内循环为 0
内循环为 0
内循环为 0
内循环为 0
内循环为 0
内循环为 0
内循环为 0
内循环为 0
内循环为 0
内循环为 0
内循环为 0
内循环为 0
内循环为 0
内循环为 0
内循环为 0
内循环为 0
内循环为 0
内循环为 0
内循环为 0
内循环为 0
内循环为 0
内循环为 0
内循环为 0
内循环为 0
Traceback (most recent call last):
  File "<pyshell#5>", line 2, in <module>
    print("内循环为",i)
KeyboardInterrupt
i=0
while i<=5:
    print("内循环为",i)
    i=i+1
else:
    print("外循环为",i)

    
内循环为 0
内循环为 1
内循环为 2
内循环为 3
内循环为 4
内循环为 5
外循环为 6
i=1
while i<5:
    print("内循环是",i)
    if i==2
    
SyntaxError: expected ':'
i=1
while i<5:
    print("内循环是",i)
    if i==2:
        break
else:
    print("外循环是",i)

    
内循环是 1
内循环是 1
内循环是 1
内循环是 1
内循环是 1
内循环是 1
内循环是 1
内循环是 1
内循环是 1
内循环是 1
内循环是 1
内循环是 1
内循环是 1
内循环是 1
内循环是 1
内循环是 1
内循环是 1
内循环是 1
内循环是 1
内循环是 1
内循环是 1
内循环是 1
内循环是 1
内循环是 1
内循环是 1
内循环是 1
内循环是 1
内循环是 1
内循环是 1
内循环是 1
内循环是 1
内循环是 1
内循环是 1
内循环是 1
内循环是 1
内循环是 1
内循环是 1
内循环是 1
内循环是 1Traceback (most recent call last):
  File "<pyshell#23>", line 2, in <module>
    print("内循环是",i)
KeyboardInterrupt
i=1
while i<5:
    print("内循环是",i)
    if i==2:
        break
    i=i+1
else:
    print("外循环是",i)

内循环是 1

内循环是 2
i=1
while i=1:
    
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
i=1
while i<=9:
    j=1
    while j<=i:
        print(j,"*",i,j*i,end="")
        j+=1
    print()
    i=i+1

    
1 * 1 1
1 * 2 22 * 2 4
1 * 3 32 * 3 63 * 3 9
1 * 4 42 * 4 83 * 4 124 * 4 16
1 * 5 52 * 5 103 * 5 154 * 5 205 * 5 25
1 * 6 62 * 6 123 * 6 184 * 6 245 * 6 306 * 6 36
1 * 7 72 * 7 143 * 7 214 * 7 285 * 7 356 * 7 427 * 7 49
1 * 8 82 * 8 163 * 8 244 * 8 325 * 8 406 * 8 487 * 8 568 * 8 64
1 * 9 92 * 9 183 * 9 274 * 9 365 * 9 456 * 9 547 * 9 638 * 9 729 * 9 81
i+1
11
i=1
while i<=9:
    j=1
    while j<=i:
        print(j,"*",i,"="j*i,end="")
        j+=1
    print()
    i=i+1


    
SyntaxError: invalid syntax. Perhaps you forgot a comma?

i=1
while i<=9:
    j=1
    while j<=i:
        print(j,"*",i,"=",j*i,end="")
        j+=1
    print()
    i=i+1

    
1 * 1 = 1
1 * 2 = 22 * 2 = 4
1 * 3 = 32 * 3 = 63 * 3 = 9
1 * 4 = 42 * 4 = 83 * 4 = 124 * 4 = 16
1 * 5 = 52 * 5 = 103 * 5 = 154 * 5 = 205 * 5 = 25
1 * 6 = 62 * 6 = 123 * 6 = 184 * 6 = 245 * 6 = 306 * 6 = 36
1 * 7 = 72 * 7 = 143 * 7 = 214 * 7 = 285 * 7 = 356 * 7 = 427 * 7 = 49
1 * 8 = 82 * 8 = 163 * 8 = 244 * 8 = 325 * 8 = 406 * 8 = 487 * 8 = 568 * 8 = 64
1 * 9 = 92 * 9 = 183 * 9 = 274 * 9 = 365 * 9 = 456 * 9 = 547 * 9 = 638 * 9 = 729 * 9 = 81
1 * 9 = 92 * 9 = 183 * 9 = 274 * 9 = 365 * 9 = 456 * 9 = 547 * 9 = 638 * 9 = 729 * 9 = 81
SyntaxError: cannot assign to expression
i=1
while i<=9:
    j=1
    while j<=i:
        print(j,"*",i,"=",j*i,end=" ")
        j+=1
    print()
    i=i+1

1 * 1 = 1 
1 * 2 = 2 2 * 2 = 4 
1 * 3 = 3 2 * 3 = 6 3 * 3 = 9 
1 * 4 = 4 2 * 4 = 8 3 * 4 = 12 4 * 4 = 16 
1 * 5 = 5 2 * 5 = 10 3 * 5 = 15 4 * 5 = 20 5 * 5 = 25 
1 * 6 = 6 2 * 6 = 12 3 * 6 = 18 4 * 6 = 24 5 * 6 = 30 6 * 6 = 36 
1 * 7 = 7 2 * 7 = 14 3 * 7 = 21 4 * 7 = 28 5 * 7 = 35 6 * 7 = 42 7 * 7 = 49 
1 * 8 = 8 2 * 8 = 16 3 * 8 = 24 4 * 8 = 32 5 * 8 = 40 6 * 8 = 48 7 * 8 = 56 8 * 8 = 64 
1 * 9 = 9 2 * 9 = 18 3 * 9 = 27 4 * 9 = 36 5 * 9 = 45 6 * 9 = 54 7 * 9 = 63 8 * 9 = 72 9 * 9 = 81 
day=1
hour=1
while day<=7:
    while hour<=8:
        if hour==8：
        
SyntaxError: invalid character '：' (U+FF1A)
day=1
hour=1
while day<=7:
    while hour<=8:
        if hour==8:
            break
print("今天我一定要学习8小时")
SyntaxError: invalid syntax
day=1
hour=1
while day<=7
SyntaxError: expected ':'
day=1
hour=1
while day<=7:
    while hour<=8；
    
SyntaxError: invalid character '；' (U+FF1B)
day =1
hour=1
while day<=7
SyntaxError: expected ':'
day=1
hour=1
while day<=7:
    while hour<=8:
        print("今天我一定学习8个小时")
        hour=hour+1
        if hour>1:
            break
    day=day+1

    
今天我一定学习8个小时
今天我一定学习8个小时
今天我一定学习8个小时
今天我一定学习8个小时
今天我一定学习8个小时
今天我一定学习8个小时
今天我一定学习8个小时
day=1
hour=1
while day<=7:
    while hour<=8:
        print("今天我要学习8个小时")
        hour=hour+1
        if hour>1:
            break
    day=day+1

    
今天我要学习8个小时
今天我要学习8个小时
今天我要学习8个小时
今天我要学习8个小时
今天我要学习8个小时
今天我要学习8个小时
今天我要学习8个小时
day=1
hour=1
while day<=7
SyntaxError: expected ':'
day=1
hour=1
while day<=7:
    while hour<=8:
        print("今天我要学习8小时")
        hour=hour+1
        if hour>1:
            break
    day=day+1

    
今天我要学习8小时
今天我要学习8小时
今天我要学习8小时
今天我要学习8小时
今天我要学习8小时
今天我要学习8小时
今天我要学习8小时
for each in"coconut":
    print(each)

    
c
o
c
o
n
u
t
for each in"like":
    print(each)

    
l
i
k
e
for each in"qujingru":
    print(each)

    
q
u
j
i
n
g
r
u
i=0
while i<len("like"):
    print("like"[i])
    i+=1

    
l
i
k
e
i=0
while i<len("ilikeit"):
    print("ilikeit"[1])
    i=i+1

    
l
l
l
l
l
l
l
i=0
while i<len("coconut"):
    print("coconut"[i])
    i=i+1

    
c
o
c
o
n
u
t
sum=0
for i in 1000000:
    sum=sum+i

    
Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    for i in 1000000:
TypeError: 'int' object is not iterable
for i in range(10):
    print(i)

    
0
1
2
3
4
5
6
7
8
9
for i in range(11):
    print(i)

    
0
1
2
3
4
5
6
7
8
9
10
for i in range(5,10)
SyntaxError: expected ':'
for i in range(5,10):
    print(i)

    
5
6
7
8
9
for i in range(5,10,2)
SyntaxError: expected ':'
for i in range(5,10,2):
    print(i)

    
5
7
9
for i in range(10,5,-2)
SyntaxError: expected ':'
for i in range(10,5,-2):
    print(i)

    
10
8
6
sum=0
for i in range(1000001)；
SyntaxError: invalid character '；' (U+FF1B)
sum=0
for i in range(1000001):
    sum=sum+i
print(sum)
SyntaxError: invalid syntax

sum=0
while i in range(10000001):
    sum=sum+1
print(i)
SyntaxError: invalid syntax
sum=0
while i in range(10000001):
    sum=sum+1
print(sum)
SyntaxError: invalid syntax
sum = 0
for i in range(1000001):
    sum += i
print(sum)
SyntaxError: multiple statements found while compiling a single statement
sum=0

for i in range(1000001):
    sum += i
print(sum)
SyntaxError: invalid syntax
sum=0
for i in range(1000001):
    sum=sum+1
print(sum)
SyntaxError: invalid syntax
sum=0
for i in range(1000001):
    sum=sum+1


print(sum)
1000001
for n in range(2,10):
    for x in range(2,n):
        if n%x==0:
            print(n,"=",x,"*",n//x)
            break
    else:
        print(n,"是一个素数")

        
2 是一个素数
3 是一个素数
4 = 2 * 2
5 是一个素数
6 = 2 * 3
7 是一个素数
8 = 2 * 4
9 = 3 * 3
9 = 3 * 3
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
for n in range(2,10):
    for x in range(2,n):
        if n%x==0:
            print(n,"=",x,"*",n/x)
    print(n,"是一个素数")

    
2 是一个素数
3 是一个素数
4 = 2 * 2.0
4 是一个素数
5 是一个素数
6 = 2 * 3.0
6 = 3 * 2.0
6 是一个素数
7 是一个素数
8 = 2 * 4.0
8 = 4 * 2.0
8 是一个素数
9 = 3 * 3.0
9 是一个素数
for n in range(2,10):
    for x in range(2,n):
        if n%x==0:
            print(n,"=",x,"*",n//x)
    print(n,"是一个素数")

    
2 是一个素数
3 是一个素数
4 = 2 * 2
4 是一个素数
5 是一个素数
6 = 2 * 3
6 = 3 * 2
6 是一个素数
7 是一个素数
8 = 2 * 4
8 = 4 * 2
8 是一个素数
9 = 3 * 3
9 是一个素数
for n in range(2,10):
    for x in range(2,n):
        if n%x==0:
            print(n,"=",x,"*",n//x)
            break
    print(n,"是一个素数")

    
2 是一个素数
3 是一个素数
4 = 2 * 2
4 是一个素数
5 是一个素数
6 = 2 * 3
6 是一个素数
7 是一个素数
8 = 2 * 4
8 是一个素数
9 = 3 * 3
9 是一个素数
for n in range(2,10):
    for x in range(2,n):
        if n%x==0:
            print(n,"=",x,"*",n//x)
            break
    else:
        print(n,"是一个素数")

    
2 是一个素数
3 是一个素数
4 = 2 * 2
5 是一个素数
6 = 2 * 3
7 是一个素数
8 = 2 * 4
9 = 3 * 3
for n in range(2,10):
    for x in range(2,n):
        if n%x==0:
            print(n,"=",x,"*",n/x)
            break
    else:
        print(n,"是一个素数")

        
2 是一个素数
3 是一个素数
4 = 2 * 2.0
5 是一个素数
6 = 2 * 3.0
7 是一个素数
8 = 2 * 4.0
9 = 3 * 3.0
for n in range(2,10)
SyntaxError: expected ':'
for n in range(2,10):
    for x in range(2,n):
        if n%x==0:
            print(n,"=",x,"*",n//x)
            break
     else:
         
SyntaxError: unindent does not match any outer indentation level
for n in range(2,10):
    for x in range(2,n):
        if n%x==0:
            print(n,"=",x,"*",n//x)
            break
     else:
         
SyntaxError: unindent does not match any outer indentation level
for n in range(2,10):
    for x in range(2,n):
        if n%x==0:
            print(n,"=",x,"*",n//x)
            break
    else:
        print(n,"是质数")

        
2 是质数
3 是质数
4 = 2 * 2
5 是质数
6 = 2 * 3
7 是质数
8 = 2 * 4
9 = 3 * 3
[1,2,3,4,5]
[1, 2, 3, 4, 5]
[1,2,3,4,5,"我爱高等数学"]
[1, 2, 3, 4, 5, '我爱高等数学']
love=[1,2,3,4,5,"我爱高等数学"]
print(love)
[1, 2, 3, 4, 5, '我爱高等数学']
for each in rhyme:
...     print(each)
... 
...     
Traceback (most recent call last):
  File "<pyshell#214>", line 1, in <module>
    for each in rhyme:
NameError: name 'rhyme' is not defined
>>> for each in love:
...     print(each)
... 
...     
1
2
3
4
5
我爱高等数学
>>> love[0]
1
>>> love[3]
4
>>> love[5]
'我爱高等数学'
>>> length = len(love)
>>> love[length - 1]
'我爱高等数学'
>>> length=len(love)
>>> love[length-1]
'我爱高等数学'
>>> love[-1]
'我爱高等数学'
>>> love[:3]
[1, 2, 3]
>>> love[3:]
[4, 5, '我爱高等数学']
>>> love[length-1]
'我爱高等数学'
>>> love[-2]
5
>>> love[:3]
[1, 2, 3]
>>> love[3:]
[4, 5, '我爱高等数学']
