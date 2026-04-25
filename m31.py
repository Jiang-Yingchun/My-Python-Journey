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
txt=txt.lower()
for ch in ',./!"':
    txt =txt.replace(ch," ")#这解释为，当ch有',./!"',就把char中的这些玩意换成空格
words=txt.split()#解释为把txt的每一个单词都分开
print(words)
#文本处理，分割单词，去除标点符号