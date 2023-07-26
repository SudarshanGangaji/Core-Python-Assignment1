# WAP to calculate total salary of employee based on basic, 
# da=10% of basic, ta=12% of basic, hra=15% of basic.

Basic = int(input("Enter basic salary: "))

DA = int(input("Enter Dearness Allowances: "))
TA = int(input("Enter Travel Allowances: "))
HRA = int(input("Enter House Rent Allowances: "))

#Allowances = DA + TA + HRA
total_allowances= Basic * ((DA/100)+(TA/100)+(HRA/100))
Total_Salary = Basic + total_allowances

print("Total Salary of employee: ",Total_Salary)
