#Create a string from given string where first and last characters exchanged.
str1 = str(input("enter the string = "))
print(str1[-1:] + str1[1:-1] + str1[:1])