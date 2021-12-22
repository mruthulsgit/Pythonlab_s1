a=input("enter a list of numbers: ")
l=a.split()
l=list(map(int,l))
for i in range(len(l)):
    if(l[i]>100):
        l[i]='over'
print(l)        


