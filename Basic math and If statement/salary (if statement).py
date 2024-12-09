gross_salary = float(input("Enter gross salary: "))

if gross_salary > 120000:
    commission = (gross_salary - 120000) *.10
    total_salary = gross_salary + commission
else:
    total_salary = gross_salary

tax = total_salary *.18

net_salary = total_salary - tax

print("Gross salary: ", gross_salary,)
print("Commission: ", commission,)
print("Total income: ", total_salary,)
print("Tax: ", tax,)
print("Net Salary: ", net_salary, ".f2")


