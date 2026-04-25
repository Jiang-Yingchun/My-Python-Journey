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
for ch in txt:
    if ch==',.?!"':
        txt=txt.replace(ch," ")
words=txt.split()
counts={}
for word in words:
    counts[word]=counts.get(word,0)+1

items =list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
# 就是把counts理解为字典，比如你去查询新华字典，你搜水性杨花，他词典里就是水性杨花：bababab,所以说对应到大蟒蛇上，counts对应的也是某个词：3（这个3是次数），然后items（）就是给词典搞了一个括号括起来，list翻译为清单，就是把我刚才说的一堆东西搞成列表的形式
# sort就是分类排序，然后括号对排序进一步详细说明
for i in range(10):
    word,count=items[i]
    print(f"{word:<10} {count:5}")

