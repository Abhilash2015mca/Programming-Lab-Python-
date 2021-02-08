#write apython program to find the HCF and LCM of 2 numbers
def HCF(x,y):
    if(x>y):
        l = x
        s = y
    if(y>x):
        l = y
        s = x
    while(s):
      l,s = s, l%s
      return l
def LCM(x,y):
    lcm = (x*y)/hcf
    return lcm
n = int(input("Enter the First Number"))
m = int(input("Enter the Second Number"))
hcf = HCF(n,m)
print("HCF = ",hcf)
print("LCM = ", LCM(n,m))