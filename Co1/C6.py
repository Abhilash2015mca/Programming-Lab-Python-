#Store a list of first names. Count the occurrences of ‘a’ within the list
names = []
y = 0
for x in range(0,3):
    a = input("enter the first name = ")
    names.append(a)  
    y += a.count("a")+a.count("A")
print("No. of Occurence of a in the list", names, "is", y)        
