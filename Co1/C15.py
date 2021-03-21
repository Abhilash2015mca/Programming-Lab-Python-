#Print out all colors from color-list1 not contained in color-list2.
lst1 = []
lst2 = []
print("List 1")
for x in range(0,5):
    a = str(input("Enter the Colour = "))
    lst1.append(a)
print("List 2")
for x in range(0,5):
    a = str(input("Enter the Colour  = "))
    lst2.append(a)    
print(lst1.difference(lst2))