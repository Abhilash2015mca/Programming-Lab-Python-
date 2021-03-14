def palindrome(s):
    return s==s[::-1]

s = str(input())
if palindrome(s):
     
    print("Yes")
else:
    print("No")
