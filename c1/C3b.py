#Square of N numbers.
lst = []
lst2 = []
n =  int(input("Enter the number of elements : "))
print("Enter the elements")
for x in range(0,n):
    a = int(input())
    lst.append(a)
for num in lst:
    a = num * num
    lst2.append(a)

print("new list =", lst2)
