Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:01:40) [MSC v.1944 32 bit (Intel)] on win32
Enter "help" below or click "Help" above for more information.
>>> if "今天是晴天"=="今天是阴天"
SyntaxError: expected ':'
>>> if "今天是晴天"=="今天是阴天"
SyntaxError: expected ':'
>>> if "今天是晴天"=="今天是阴天"：
SyntaxError: invalid character '：' (U+FF1A)
>>> if "今天是晴天"=="今天是阴天"
SyntaxError: expected ':'
>>> if "今天是晴天"=="今天是阴天"：
SyntaxError: invalid character '：' (U+FF1A)
>>> if "今天是晴天"=="今天是阴天":
...     print("今天是晴天")
... else:
...     print("今天不是晴天")
... 
...     
今天不是晴天
