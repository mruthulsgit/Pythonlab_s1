c=input("enter a colour: ")
b= c.split(' ')
b[0],b[-1]=b[-1],b[0]
print("the rearranged is",b)
