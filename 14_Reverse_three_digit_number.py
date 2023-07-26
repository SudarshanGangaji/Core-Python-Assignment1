#Write a program to reverse three digit number.

num = int(input("Enter number: "))

a = num % 10
b = num // 10
c = b % 10
x = b // 10

Reverse = (a*100)+(c*10)+x

print("Reverse digit number: ", Reverse)