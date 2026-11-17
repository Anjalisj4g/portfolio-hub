# PayrollPro - basic salary calculation
name = input("Employee name: ")
basic = float(input("Basic salary: "))

hra = basic * 0.20
travel_allowance = basic * 0.05
tax = basic * 0.10
net_salary = basic + hra + travel_allowance - tax

print("\nSALARY SLIP")
print("Employee:", name)
print("Basic salary:", basic)
print("HRA:", hra)
print("Travel allowance:", travel_allowance)
print("Tax deduction:", tax)
print("Net salary:", net_salary)
