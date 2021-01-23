#function to check whether a number is perfect or not
def perfect(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    if sum == n:
        return True
    else:
        return False   
x = int(input("Enter the Number = "))
print(perfect(x))