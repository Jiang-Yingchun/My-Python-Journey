Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:01:40) [MSC v.1944 32 bit (Intel)] on win32
Enter "help" below or click "Help" above for more information.
>>> import copy
>>> x=[[1,2,3].[4,5,6],[7,8,9]]
SyntaxError: invalid syntax
>>> x=[[1,2,3],[4,5,6],[7,8,9]]
>>> y=copy.copy(x)
>>> x[1][2]=0
>>> 
>>> x[1][1]=0
>>> x
[[1, 2, 3], [4, 0, 0], [7, 8, 9]]
>>> x=[[1,2,3],[4,5,6],[7,8,9]]
>>> y=copy.copy(x)
>>> y
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> x[1][1]=0
>>> x
[[1, 2, 3], [4, 0, 6], [7, 8, 9]]
>>> y
[[1, 2, 3], [4, 0, 6], [7, 8, 9]]
>>> x=[[1,2,3],[4,5,6],[7,8,9]]
>>> y=copy.deepcopuy(x)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    y=copy.deepcopuy(x)
AttributeError: module 'copy' has no attribute 'deepcopuy'. Did you mean: 'deepcopy'?
>>> y=copy.deepcopy(x)
>>> x[1][1]
5
>>> x[1][1]=0
>>> x
[[1, 2, 3], [4, 0, 6], [7, 8, 9]]
>>> y
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
