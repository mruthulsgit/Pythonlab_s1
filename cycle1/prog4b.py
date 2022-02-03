a=input("enter a numbers: ")
a=a.split()
a=list(map(int,a))
c = []
for i in a:
	if i > 100:
		c.append("over")
	else:
                c.append(i)
print(c)	
