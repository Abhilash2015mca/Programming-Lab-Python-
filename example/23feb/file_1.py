#Create a txt file write python code to find no. of lines present in text file.
str = "Are\nyou\nHappy"
f = open("1.txt",'w')
f.write(str)
f.close()
f = open("1.txt",'r')
y = f.readlines()
print(len(y))
