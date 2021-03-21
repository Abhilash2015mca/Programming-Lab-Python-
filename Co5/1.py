#Write a Python program to read a file line by line and store it into a list
Fw = open("content.txt","a")
Fw.write("Hai! Everyone \nGood Morning\nGood Evening")
Fw.close()
str = ""
readF = open("content.txt","r")
for line in readF:
    str +=line
print(str)    
readF.close()