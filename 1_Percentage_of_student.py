# WAP to calculate the percentage of student based on marks of any 5 subjects.

S1 = int(input("Enter English Marks: "))
S2 = int(input("Enter Math Marks: "))
S3 = int(input("Enter Computer Marks: "))
S4 = int(input("Enter Physics Marks: "))
S5 = int(input("Enter Chemistry Marks: "))

total = S1 + S2 + S3 + S4 + S5

percentage = (total / 500) * 100

print("Percentage: ",percentage)