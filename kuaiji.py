def calculate_sector_1():
    central_angle_1 = 160
    radius_1 = 30
    sector_area_1 = central_angle_1 / 360 * 3.14 * radius_1 ** 2
    print(f"此扇形面积为：{sector_area_1}")#这里f的作用就是让大蟒蛇知道，这里要输出{sector_area_1}的具体数值
calculate_sector_1()
def calculate_sector(central_angle,radius):#def是定义函数的关键字
    sector_area = central_angle/360*3.14*radius**2
    print(f"此扇形面积为：{sector_area}")
calculate_sector(central_angle=160,radius=30)
def calculate_BMI(weight,height):
    BMI=weight/height**2
    print(f"您的体脂率为{BMI}")
calculate_BMI(weight=60,height=1.84)
calculate_BMI(weight=45,height=1.60)
