Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:01:40) [MSC v.1944 32 bit (Intel)] on win32
Enter "help" below or click "Help" above for more information.
3/2
1.5
3//2
1
-3//2
-2
3%2
1
6%2
0
divmod(3,2)
(1, 1)
(1, 1)
(1, 1)
(1, 1)
(1, 1)

#943070#
#就是说divmod（,）前者是地板除，后者是取余。前者是地板除，后者是取余#
divmod(4,7)
(0, 4)
divmod(9,4)
(2, 1)
a=-123
abs(a)
123
b=-234
abs(b)
234
c=98
abs(c)
98
#abs()是求绝对值，而不是求相反数，比如q=123,abs(q)结果还是123，而不是-123#
t=1+3j
abs(t)
3.1622776601683795
#对于共轭复数，abs（）就是用来计算模长#
int(3.14)
3
int(9.99)
9
float('520')
520.0
float(234.99)
234.99
float(1E5)
100000.0
complex(2,3)
(2+3j)
complex(4,5)
(4+5j)
complex(6,7)
(6+7j)
3**6
729
pow(3,6)
729
#就是说a**b就是求A的b次方等于多少，pow（,）#
#同时，pow(a,b)也是表示a的b次方等于多少#


bool(250)
True
bool("假")
True
bool
<class 'bool'>
bool(False)
False
bool("")
False
bool(" ")
True
bool(520)
True
bool(0)
False
bool(0.0)
False
bool(0j)
False
False
False

False
False

False
False

if 666>777:
    print("666大于777")
else:
    print("666小于777")

    
666小于777
if bool(666)
SyntaxError: expected ':'
if bool(777):
    print("777 is true")
else:
    print("777 is false")

    
777 is true
777 is true
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    777 is true
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> 
>>> 
>>> 2==true
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    2==true
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> 5==True
False
>>> 9==False
False
>>> True==False
False
>>> True+False
1
>>> 1
1
>>> 
>>> 1==True
True
>>> 0==False
True
>>> True*False
0
>>> 4>9 and 3<5
False
>>> 3>2 and 4>1
True
>>> 3>2 or 3<1
True
>>> 3>5 or 3<2
False
>>> not True
False
>>> not False
True
>>> not 0
True
>>> 3 and 4
4
>>> 4 or 5
4
