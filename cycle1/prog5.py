count=0
a=input("enter the 1st list of numbers sepereted by comas : ")
b=input("enter the 2nd list of numbers sepereted by comas : ")
a=a.split(',')
b=b.split(',')
a=list(map(int,a))
b=list(map(int,b))
if len(a)==len(b):
    print("both list are in same length")
else :
    print("both list are not in same length")
if sum(a)==sum(b):
    print("sum of both list are equal")
else :
    print("sum of both aren't equal")
for i in a:
    if i in b:
        print(i,"occure in both")
        count+=1
if count==0:
    print("no values occure in both lists")


            
    
