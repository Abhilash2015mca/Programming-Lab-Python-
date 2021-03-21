#Add ‘ing’ at the end of a given string. If it already ends with ‘ing’, then add ‘ly’
string=input("Enter the string = ")
print("The output string is given below")
if string[-3:]=="ing":
    print(string+"ly")
else:
    print(string+"ing")