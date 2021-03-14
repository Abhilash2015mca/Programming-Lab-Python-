#Create a class Rectangle with private attributes length and width. Overload ‘<’ operator to 
#compare the area of 2 rectangles.
class rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area():
        self.area=self.length*self.width    
        return self.area
    def __gt__(self, other): 
        if(self.area>other.area): 
            return True
        else: 
            return False    
rec1=rectangle(3,5)
rec2=rectangle(4,7)
if(rec1>rec2):
    print("area of first rectangle is more")
else:
    print("Area of second rectangle is more")                