grade_dict={"大少爷":80.345,"墨镜":70.568,"大小姐":99.098,"西装":44.2367}
for name,grade in grade_dict.items():
    print("{0}的成绩为：{1:.2f}".format(name,grade))
contacts=["老余","老张","老徐","老毕","老梁","老毛","老王","老万"]
for name in contacts:
    message_contact =name + ": 岁始只乐，点翠画柳喜开颜。\n云开雾散，良辰美景共团圆。\n祝福"+name+"及家人新年快乐，平安顺遂，虎年大吉"
    print(message_contact)
year = "马"
name = "朋友"
message_content=''' 
律回春渐，新元肇启。
新岁甫至，福气东来。
金{year}贺岁，欢乐祥瑞。
金{year}敲门，五福临门。
给{name}及家人拜年啦!
新春快乐，{year}年大吉'''.format(year=year,name=name)
print(message_content)
name1="林如欣"
year1="马"
message_content=f'''  
律回春渐，新元肇启。
新岁甫至，福气东来。
金{year1}贺岁，欢乐祥瑞。
金{year1}敲门，五福临门。
给{name1}及家人拜年啦!
新春快乐，{year1}年大吉
'''
print(message_content)
name2="小林如欣"
year2="猪"
message_content='''  
律回春渐，新元肇启。
新岁甫至，福气东来。
金{year1}贺岁，欢乐祥瑞。
金{year1}敲门，五福临门。
给{name1}及家人拜年啦!
新春快乐，{year1}年大吉
'''.format(year1=year2,name1=name2)
print(message_content)
gpa_dict={"小林":3.345,"小如":3.567,"小欣":2.345,"小林如欣":3.6665}
for name,gpa in gpa_dict.items():
    #因为你定义“小林”：3.456。这是键值的写法，你要输出键值就要用for in 循环的.items()形式
    print("{0}你好，你当前的绩点为{1}".format(name,gpa))




