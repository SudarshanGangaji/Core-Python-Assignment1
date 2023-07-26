#Write a program to accept an integer amount from user and tell minimum number of notes needed 
# for representing that amount. 
# (Hint – Consider 450 -> 4*100 + 50*1 -> 2 : 5 notes)

range = (2000,500,200,100,50,20,10,5)

amount = int(input("Enter Amount: "))

for i in range:
    count = amount // i
    print("Note Value : ",i,'\tnumber of notes' ,count)
    amount = amount % i