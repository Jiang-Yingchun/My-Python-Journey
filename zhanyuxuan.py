class Employee:
    def __init__(self,name,id1):
        self.name=name
        self.id1=id1
    def print_info(self):
         print(f"员工名字:{self.name},学号{self.id1}")
class FullTimeEmployee(Employee):
    def __init__(self,name,id1,monthly_salary):
        super().__init__(name,id1)
        self.monthly_salary=monthly_salary
    def calculate_monthly_pay(self):
        return self.monthly_salary
class PartTimeEmployee(Employee):
    def __init__(self,name,id1,daily_salary,work_days):
        super().__init__(name,id1)
        self.daily_salary=daily_salary
        self.work_days=work_days
    def calculate_daily_pay(self):
        return self.daily_salary*self.work_days
zhangsang=FullTimeEmployee("张三","1002",6000)
lisi=PartTimeEmployee("李四","1003",250,12)
zhangsang.print_info()
lisi.print_info()
print(zhangsang.calculate_monthly_pay())
print(lisi.calculate_daily_pay())





