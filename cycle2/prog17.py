a=int(input("Enter the year"))
if a%400==0 or a%4==0 and a%100!=0:
    print("leap year")  
else:
    print("Not a leap year")
