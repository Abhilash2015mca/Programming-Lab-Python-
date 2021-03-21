#From a list of integers, create a list removing even numbers.
lst1=[]
lst2=[]
n =int(input("enter the number of integers = "))
for x in range(0,n):
    y = int(input("Enter the integer = "))
    lst1.append(y)
    if y%2!=0:
        lst2.append(y)
print("List with even numbers",lst1)
print("List without even numbers",lst2)
