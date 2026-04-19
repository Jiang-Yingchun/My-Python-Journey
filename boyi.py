try:
    user_height=float(input("请输入你的身高，单位米"))
    user_weight=float(input("请输入你的体重，单位千克"))
    user_BMI=user_weight/user_height**2
except ValueError:
    print("输入为不合理数字,请重新运转程序,重新输入")
except ZeroDivisionError:
    print("身高不能为0,请重新运转程序,重新输入")
except:
    print("未知错误类型,请重新运转程序,重新输入")
else:
    print("您的BMI为",user_BMI)
finally:
    print("运行结束")


