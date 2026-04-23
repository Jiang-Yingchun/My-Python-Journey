# 从键盘输入 3 个点的坐标，每个点的横、纵坐标用空格分隔，一共 6 个数字，对应变量 x0 y0 x1 y1 x2 y2。
# 计算由这三个点构成的三角形的三条边长，再求出三角形的周长，屏幕输出周长，保留 2 位小数
import math
x0,y0,x1,y1,x2,y2=map(float,input("请输入三个坐标").split())
distance1=math.sqrt((x0-x1)**2+(y0-y1)**2)
distance2=math.sqrt((x0-x2)**2+(y0-y2)**2)
distance3=math.sqrt((x1-x2)**2+(y1-y2)**2)
total_distance =distance1+distance2+distance3
print(f"{total_distance:.2f}")