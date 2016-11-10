user=input("Hourly wage?")
Hourlywage=int(user)

user=input("Many hours did you work?")
time=int(user)

Payroll = Hourlywage * time

fmt="""
Hourlywage{0}yen,{1}hour work,
Payroll is {2}yen
"""

desc=fmt.format(Hourlywage,time,Payroll)
print(desc)
