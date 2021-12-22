a=input("enter the list of numbers seperated by coma: ");
a=a.split(',')
a=list(map(int,a))
c=[i for i in a if i%2 !=0]
print(c)




