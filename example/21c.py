#Function to find common elements present in two lists
def common(lst1,lst2):
    com = []
    for x in lst1:
        for y in lst2:
            if x == y:
                com.append(x)
    return com
p = []
q = []
n = int(input("enter the number of element in list 1 = "))
for x in range (0,n):
    a = input("enter the element = ")
    p.append(a)    
m = int(input("enter the number of element in list 2 = ")) 
for x in range (0,m):
    a = input("enter the element = ")
    q.append(a)  
b = common(p,q)    
print("Common elements in Two list are", b)