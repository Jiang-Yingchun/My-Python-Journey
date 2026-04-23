# 从键盘输入4个数字，各数字采用空格分隔，对应为变量x0,y0,x1,y1。计算两点（x0,y0）和（x1,y1)之间的距离，屏幕输出这个距离，保留2位小数。
# 例如：键盘输入：0135
# 口
# 屏幕输出：5.00
import math
x0,y0,x1,y1=map(float,input().split())
distance=math.sqrt((x1-x0)**2+(y1-y0)**2)
print(f"{distance:.2f}")