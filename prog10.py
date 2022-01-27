num1=int(input("enter num1:"))
num2=int(input("enter num2:"))
if num1>num2:
	lim=num2
else :
	lim=num1
for i in range(1,lim+1):
	if(num1%i==0 and num2%i==0):
		gcd=i
print(gcd,"is the gcd of ",num1,"and",num2)