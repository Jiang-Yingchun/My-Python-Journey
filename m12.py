# 使用 Python 的turtle库，通过turtle.fd()和turtle.seth()函数，绘制一个边长为 180 的正六边形。
# 六边形的箭头方向需与示例图（箭头在左侧，初始朝向左上方）完全一致。
# 解题关键提示：
import turtle
turtle.seth(180)
turtle.fd(180)
turtle.seth(120)
turtle.fd(180)
turtle.seth(60)
turtle.fd(180)
turtle.seth(0)
turtle.fd(180)
turtle.seth(-60)
turtle.fd(180)
turtle.seth(-120)
turtle.fd(180)
turtle.done()