#WAP Find the sum of three digit number.

num = int(input("Enter number: "))

a = num % 10
b = num // 10
c = b % 10
x = b // 10

sum = a + c + x
print("Sum of digits: ", sum)