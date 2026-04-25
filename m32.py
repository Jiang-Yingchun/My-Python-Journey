txt="""Shall I compare thee to a summer’s day?
Thou art more lovely and more temperate:
Rough winds do shake the darling buds of May,
And summer’s lease hath all too short a date:
Sometime too hot the eye of heaven shines,
And often is his gold complexion dimm’d;
And every fair from fair sometime declines,
By chance or nature’s changing course untrimm’d;
But thy eternal summer shall not fade,
Nor lose possession of that fair thou owest;
Nor shall Death brag thou wander’st in his shade,
When in eternal lines to time thou growest:
So long as men can breathe or eyes can see,
So long lives this, and this gives life to thee."""
txt=txt.lower()#这行代码的意思是把字母全部转换为小写字母txt=txt.lower(),（）是方法名，方法名要用（）意味着要执行这个方法名
for ch in txt:
    if ch==',./!"':
        txt=txt.replace(ch," ")
words=txt.split()
print(words)