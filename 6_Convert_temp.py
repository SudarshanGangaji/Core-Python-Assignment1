#WAP to Convert temp from Celsius to Fahrenheit. (C/5 = (F-32)/9)

celsius = float(input("Enter temperature in celsius: "))
fahrenheit = (celsius * 9/5) + 32

print("Temperature in Fahrenheit: ",fahrenheit)