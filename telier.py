Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:01:40) [MSC v.1944 32 bit (Intel)] on win32
Enter "help" below or click "Help" above for more information.
>>> x=[1,2,3]
>>> y=x
>>> x[1]=1
>>> x
[1, 1, 3]
>>> y
[1, 1, 3]
>>> x=[1,2,3]
>>> y=x.copy()
>>> x
[1, 2, 3]
y
>>> 
>>> y
[1, 2, 3]
>>> x=[1,2,3]
>>> y=x[:]
>>> x[1]=1
>>> x
[1, 1, 3]
>>> y
[1, 2, 3]
>>> x=[[1,2,3],[4,5,6],[7,8,9]]
>>> y=x.copy()
>>> x[1]=1
>>> x[1][1]=0
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    x[1][1]=0
TypeError: 'int' object does not support item assignment
>>> x=[[1,2,3],[4,5,6],[7,8,9]]
>>> t=x.copy()
>>> x[1][1]=0
>>> x
[[1, 2, 3], [4, 0, 6], [7, 8, 9]]
>>> y
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> y=x.copy()
>>> y
[[1, 2, 3], [4, 0, 6], [7, 8, 9]]
>>> t
[[1, 2, 3], [4, 0, 6], [7, 8, 9]]
