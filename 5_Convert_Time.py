#WAP to Convert the time entered in hh,min and sec into seconds.

hours = int(input("Enter hours: ")) * 3600
minutes = int(input("Enter minutes: ")) * 60
seconds = int(input("Enter seconds: "))

time = hours + minutes + seconds

print("The  amounts of seconds", time)
