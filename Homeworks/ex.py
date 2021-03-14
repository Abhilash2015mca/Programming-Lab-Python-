#amstrong number
def amstrong check(no):
    temp = no
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if num == sum:
         return 
    else:
        