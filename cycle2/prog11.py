s=input("Enter the integers:")
s=map(int,s.split(" "))
l=list(s)
l=[x for x in l if x>0]
print("the positive integers are: ",l)