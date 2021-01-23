#function to check whether string is palindrome or not without using reverse function
def palindrome(s):
    w = ""
    for i in s:
        w = i + w
    if (s == w):
        return True
    else:
        return False
s = str(input("enter the string = "))
state = palindrome(s)
if(state):
    print("String is Palindrome")
else:
     print("String is Not Palindrome")
  
   