class rectangle:
    def __init__(self,breadth,height):
        self.breadth=breadth
        self.height=height
    def area(self):
        return self.breadth*self.height
a=int(input("enter the breadth of rectangle 1:"))
b=int(input("enter the height of rectangle 1:"))
c=int(input("enter the breadth of rectangle 2:"))
d=int(input("enter the height of rectangle 2:"))
obj1=rectangle(a,b)
obj2=rectangle(c,d)
d=obj1.area()
f=obj2.area()
print("Area of the rectangle 1:",d)
print("Area of the rectangle 2:",f)
if f==d:
    print("Both rectangle are matching")
else:
    print("Both rectangle are not matching")
