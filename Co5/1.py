#Write a Python program to read a file line by line and store it into a list
str = "Are" "\n" "you" "\n" "Happy"
f = open("2.txt",'w')
f.write(str)
f.close()
f = open("2.txt",'r')
y = f.readlines()
print(len(y))
f = open("2.txt",'r')
str1 = f.readlines()
print(str1)