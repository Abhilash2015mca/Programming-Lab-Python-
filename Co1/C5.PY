#prompt the user for a list of integers. For all values greater than 100, store ‘over’ instead
lst =  []
y = 1
while y > 0 :
    x = int(input("Enter the digit = "))
    if x > 100:
        a = "Over"
    else:
        a = x
    lst.append(a)  
    print(lst)      