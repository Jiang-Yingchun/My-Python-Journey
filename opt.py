## 使用 turtle 库的 turtle.right() 函数和 turtle.fd() 函数绘制一个等腰梯形，上底 100 像素，下底 200 像素，腰长 120 像素，内角度数为 2 个 60 度、2 个 120 度。
import turtle
turtle.fd(200)
turtle.right(120)
turtle.fd(120)
turtle.right(60)
turtle.fd(100)
turtle.right(60)
turtle.fd(120)
turtle.right(120)
turtle.done()