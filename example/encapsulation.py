class Alli:
    def __init__(self):
        self.cost = 100
    def price(self):
        print("cost is less")
           
class Balli:
    def __init__(self):
        self .cost =  111
    def price(self):
        print("cost is more") 
def total(place):
    place.price()
a = Alli()
b = Balli()
total(a)
total(b)
