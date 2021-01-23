#generate +ve list of numbers from a given list of integers
lst = []
lst2 = []
n =  int(input("Enter the number of elements : "))
print("Enter the elements")
for x in range(0,n):
    a = int(input())
    lst.append(a)
for num in lst: 
	
	if num >= 0: 
           lst2.append(num)

print("positive list =", lst2)
  