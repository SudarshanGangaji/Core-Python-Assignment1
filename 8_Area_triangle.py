#WAP to calculate area of triangle and rectangle. 

#Area of Triangle
a = int(input('Enter the length of first side: '))  
b = int(input('Enter  the length of second side: '))  
c = int(input('Enter  the length of third side: '))

#Calculate the semi-perimeter
s = (a + b + c) / 2
Area = (s* (s-a) * (s-b) * (s-c)) ** 0.5

print("The area of the triangle is: ", Area)

#Area of Rectangle
l = int(input('Enter the length of a Rectangle: '))
b = int(input('Enter the breadth of a Rectangle: '))
Area = l * b

print("Area of a Rectangle is: ", Area)