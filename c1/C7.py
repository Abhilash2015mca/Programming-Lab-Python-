#Enter 2 lists of integers. Check (a) Whether list are of same length (b) whether list sums
#to same value (c) whether any value occur in both
lst1 = ['1', '2', '3', '4']
lst2 = ['3', '5', '2', '100', '12', '12']
sum1 = str(0)
sum2 = str(0)
if len(lst1) == len(lst2):
    print("both list are of equal length")
else:
    print("Two lists have unequal length") 
for x in lst1:
    sum1 = sum1 + x
for x in lst2:
    sum2 = sum2 + x
if sum1 == sum2:
    a = "equal"  
else:
    a = "not equal"  
print(" sum of two list are ", a)  
for x in lst1:
    for y in lst2:
        if x == y:
            print(y," occurs in both lst")
