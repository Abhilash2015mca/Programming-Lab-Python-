#Write a program to write a data from one file to another
str = "Hello! \nHow are you? \nWhat are you doing now? \n"
f = open("1.txt",'w')
f.write(str)
f.close()
f = open("1.txt",'r')
str2 =f.read()
f.close()
f= open("2.txt","w")
f.write(str2)
f.close()
f = open("1.txt",'r')
print(f.read())