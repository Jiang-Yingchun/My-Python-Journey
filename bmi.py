def calculate_BMI(weight,height):
    BMI=weight/height**2
    if BMI<=18.5:
        category="偏瘦"
    elif BMI<=25:
        category="正常"
    elif BMI<=30:
        category ="偏胖"
    else:
        category="肥胖"
    print(f"您的BMI为{BMI:.2f}")
    print(f"您的体脂率类型为{category}")
    return BMI
your=calculate_BMI(weight=65,height=1.90)

