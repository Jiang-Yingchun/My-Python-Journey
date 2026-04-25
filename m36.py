txt="""When, in disgrace with fortune and men's eyes,
I all alone beweep my outcast state,
And trouble deaf heaven with my bootless cries,
And look upon myself and curse my fate,
Wishing me like to one more rich in hope,
Featured like him, like him with friends possess'd,
Desiring this man's art and that man's scope,
With what I most enjoy contented least;
Yet in these thoughts myself almost despising,
Haply I think on thee, and then my state,
Like to the lark at break of day arising
From sullen earth, sings hymns at heaven's gate;
For thy sweet love remembered such wealth brings
That then I scorn to change my state with kings."""
#第一步就是把标点符号去掉
for i in txt:
    if i==',.?!"':
        txt=txt.replace(i," ")
word=txt.split()

#第二部就是把这个词语重复多少次罗列出来/
counts={}
for j in word:
    counts[j]=counts.get(j,0)+1
print(counts)

# items=list(counts.items())
# items.sort(key=lambda x:x[1],reverse=True)
# for i in range(10):
#     word,count=items[i]
#     print(f"{word:<10} {count:5}")
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    word,count=items[i]
    print(f"{word:<10} {count:>5}")
    #f"{word:<10} {count>:5}"这个意思是word左对齐，占10个位置，没有字符的用空格补齐，count是次数，就是说右对齐，占5个位置，没有字符的用
    #空格补上






