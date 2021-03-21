#Find the sum of all items in a list
list=[1,6,3,2,9,21]
sum=0
for i in range(len(list)):
    sum=sum+list[i]
print("The sum of list elements is "+str(sum))