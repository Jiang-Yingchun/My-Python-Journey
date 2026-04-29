# 题目 1：绘制正方形
# 题目描述：
# 使用 turtle.fd() 和 turtle.seth() 函数，绘制一个边长为 100 像素的正方形，效果如下（提示：正方形四个顶点的朝向分别为 0°、90°、180°、270°）。
import turtle
turtle.fd(100)
turtle.seth(90)
turtle.fd(100)
turtle.seth(180)
turtle.fd(100)
turtle.seth(-90)
turtle.fd(100)
turtle.done()