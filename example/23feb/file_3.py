#read a file and count the frequency of a word in dictionary, store occurance of each word in the form of dictonary
f=open("2.txt",'r')
str1 = f.read()
f.close()
dict = {}
for word in str1:
    if word in dict:
        dict[word] += 1
    else:
        dict[word]=1
print(dict)            