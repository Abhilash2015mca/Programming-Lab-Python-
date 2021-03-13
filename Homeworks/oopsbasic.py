class Parrot:
    species = "bird" 
    def __init__(self, name, age):
        self.name = name
        self.age = age    
    #methods
    def ageMul(self,a):
        return self.age*a    
blu = Parrot("blu",10)
woo = Parrot("woo",12)
print("Blu is a {}".format(blu.__class__.species))
print("Woo is a {}".format(woo.__class__.species))

print("{} is a {}".format(blu.name,blu.age))
print("{} is a {}".format(woo.name,woo.age))
print("ageMul = ", blu.ageMul(2))

