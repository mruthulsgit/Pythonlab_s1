la=input("enter the list of colours: ")
lb=input("enter the next list of colours: ")
la=la.split(' ')
lb=lb.split(' ')
la=set(la)
lb=set(lb)
c=la.difference(lb)
print(c)

