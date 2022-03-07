def fibonacci(num):
    a,b=0,1
    i=0
    while(i<num):
        print(a)
        a,b=b,a+b
        i=i+1
num=int(input("enter the N terms:"))
fibonacci(num)