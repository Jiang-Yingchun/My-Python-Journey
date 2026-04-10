temperature_list=[36.4,36.6,36.2,37.0,36.5,36.0,39.5,38.5,38.8]
for temperature in temperature_list:
    #for temperature in temperature_list:所以这行意思是来了一个变量temperature,然后让这个变量temperature依次赋值为 temperature_list里面的值
    if temperature >= 38:
        #挨个判断temperature这个变量的值会不会大于三十八
        print(temperature)
        print("完球了")
temperature_dict ={"111":36.4,"112":36.6,"113":36.4,"114":36.6,"115":38.5,"116":38.8}
for staff_id,temperature in temperature_dict.items():
      if temperature >= 38:
        print(staff_id)
total=0
for i in range(1,101):
    total = total +i
print(total)
s="hi"
print(len(s))
