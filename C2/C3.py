#Find the sum of all items in a list
lst =[]
n = int(input("Enter the Limi"))
li = [12,3,43,4,5,11,60]
sum=0
for x in range(0,len(li)):
    sum = sum + li[x]
print("sum of items in list = ",sum)