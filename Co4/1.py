#Create Rectangle class with attributes length and breadth and methods to find area and
#perimeter. Compare two Rectangle objects by their area
class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
a=int(input("Enter the length of the first rectangle:"))
b=int(input("Enter the breadth of the first rectangle:"))
c=int(input("Enter the length of the Second rectangle:"))
d=int(input("Enter the breadth of the Second rectangle:"))        
rect1=rectangle(a,b)
rect2=rectangle(c,d)
if rect1.area() == rect2.area():
    print("Areas of the rectangles are equal")
elif rect1.area() < rect2.area():
    print("Area of second triangle is more") 
elif rect1.area() > rect2.area():
    print("Area of first triangle is more")     