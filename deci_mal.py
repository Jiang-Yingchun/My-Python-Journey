Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:01:40) [MSC v.1944 32 bit (Intel)] on win32
Enter "help" below or click "Help" above for more information.
1234567890/3456346
357.1887449925442
6/2
3.0
i=0
while i<1:
    i=i+o.0
    
SyntaxError: invalid syntax
while i<1:
    i=i+0.1
    print(i)

    
0.1
0.2
0.30000000000000004
0.4

0.5
0.6
0.7
0.7999999999999999
0.8999999999999999
0.9999999999999999
1.0999999999999999
while i<1:
    i=i+0.1
    print(i)

    








while a<2:
    a=a+0.2
    print(a)

    
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    while a<2:
NameError: name 'a' is not defined
a=0
while a<2:
    a=a+0.2
    print(a)
    
SyntaxError: multiple statements found while compiling a single statement
a=0
while a<2:
    a=a+0.2
    print(a)
print(a)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined
>>> 
>>> a=8
>>> while a<9:
...     a=a+0.1
...     print(a)
... 
...     
8.1
8.2
8.299999999999999
8.399999999999999
8.499999999999998
8.599999999999998
8.699999999999998
8.799999999999997
8.899999999999997
8.999999999999996
9.099999999999996
>>> 0.3==0.1+0.2
False
>>> c=decimal.Decimal('0.1')
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    c=decimal.Decimal('0.1')
NameError: name 'decimal' is not defined. Did you forget to import 'decimal'?
>>> import decimal
>>> a=decimal.Decimal('0.1')
>>> b=decimal.Decimal('0.2')
>>> print(a+b)
0.3
>>> c=decimal.Decimal('0.3')
>>> a+b=c
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
>>> a+b==c
True
>>> a+b==c
True
>>> 0.7+0.3==1.0
True
>>> a=5
>>> while a<6:
...     a=a+0.1
...     print(a)
... 
    
5.1
5.199999999999999
5.299999999999999
5.399999999999999
5.499999999999998
5.599999999999998
5.6999999999999975
5.799999999999997
5.899999999999997
5.9999999999999964
6.099999999999996
import
SyntaxError: Expected one or more names after 'import'
import decimal
t=decimal.Decimal('0.9')
y=decimal.Decimal('0.4')
print(t+y)
1.3
c=decimal.Deciaml('1.3')
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    c=decimal.Deciaml('1.3')
AttributeError: module 'decimal' has no attribute 'Deciaml'. Did you mean: 'Decimal'?
c=decimal.Decimal('1.3')
t+y==c
True
1+2j
(1+2j)
x=1+2j
x.real
1.0
x.imag
2.0
u=4+789j
u.real
4.0
u.imag
789.0
