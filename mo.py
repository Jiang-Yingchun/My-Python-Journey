class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def print_info(self):
        print(f"员工名字：{self.name}，学号{self.id}")
class FullTimeEmployee(Employee):
    def __init__(self,name,id ,monthly_salary):
        super().__init__(name,id)
        self.monthly_salary=monthly_salary
    def calculate_monthly_salary(self):
        return self.monthly_salary
class PartTimeEmployee(Employee):
    def __init__(self,name,id,daily_salary,work_days):
        super().__init__(name,id)
        self.daily_salary=daily_salary
        self.work_days=work_days
    def calculate_daily_salary(self):
        return self.daily_salary*self.work_days
linruxin=FullTimeEmployee("林如欣","123456",9000)
fangxiaoling=PartTimeEmployee("方小玲","1234567890",990,34)
linruxin.print_info()
fangxiaoling.print_info()
print(linruxin.calculate_monthly_salary())
print(fangxiaoling.calculate_daily_salary())
# 反正说，无论子类父类，只要有def ,比如def __init__()括号里面一定要写self但是super().__init__()这种括号里面一定不能写self

