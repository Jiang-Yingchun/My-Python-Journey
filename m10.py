# 使用 Python 的turtle库，通过turtle.fd()和turtle.seth()函数，绘制一个边长为 150 的正三角形。
# 三角形的箭头方向需与示例图（箭头在左下角，初始朝向左上方）完全一致。
import turtle
turtle.seth(120)
turtle.fd(150)
turtle.seth(-120)
turtle.fd(150)
turtle.seth(0)
turtle.fd(150)
turtle.done()
