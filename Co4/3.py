#Create a class Rectangle with private attributes length and width. Overload ‘<’ operator to 
#compare the area of 2 rectangles.
class rectangle:
    __length=0
    __breadth=0
    __area=0
    def __init__(self,l,w):
        self.__length=l
        self.__width=w
    def area(self):
        self.__area=self.__length*self.__width
    def __gt__(self,other):
        if(self.__area>other.__area):
            return True
        else:
            return False
a=int(input("Enter the length of the first rectangle:"))
b=int(input("Enter the breadth of the first rectangle:"))
c=int(input("Enter the length of the Second rectangle:"))
d=int(input("Enter the breadth of the Second rectangle:"))            
ob1=rectangle(a,b)
ob1.area()
ob2=rectangle(c,d)
ob2.area()
if(ob1>ob2):
    print("Area of rectangle 1 is greater than area of rectangle 2")
else:
    print("Area of rectangle 2 is greater than area of rectangle 1")