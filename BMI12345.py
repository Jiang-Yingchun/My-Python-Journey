def calculate_BMI(weight,height):
    BMI =weight/height**2
    if BMI<=18.5:
        category="偏瘦"
    elif BMI<=25:
        category="正常"
    elif BMI<=30:
        category="偏胖"
    else:
        category="肥胖"
    print(f"您的BMI数值为{BMI:.2f}")
    print(f"您的体脂率为{category}")
    return BMI
calculate_BMI_your=calculate_BMI(weight=45,height=1.67)



