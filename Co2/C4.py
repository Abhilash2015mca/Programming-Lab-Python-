#Generate a list of four digit numbers in a given range with all their digits even and the 
 #number is a perfect square
import math
b=int(input("Enter range from:"))
c=int(input("Enter range to:"))
a=[]
print(b**2)
if b>999 & c<10000:
    for x in range(b,c+1):
        if x%2==0 and math.isqrt(x) ** 2 == x:
            a.append(x)
print(a)

