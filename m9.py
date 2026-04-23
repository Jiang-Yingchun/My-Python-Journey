# 使用turtle库的turtle.fd0函数和turtle.seth0函数绘制一个边长为20o的正菱形，菱形4个内角均为90度
import turtle

turtle.seth(135)
turtle.fd(200)

turtle.seth(-135)
turtle.fd(200)
turtle.seth(-45)
turtle.fd(200)
turtle.seth(45)
turtle.fd(200)
turtle.done()
