#Store a list of first names. Count the occurrences of ‘a’ within the list
name = input("Enter the name seperated by a comma:")
x = name.split(",")
c = 0
print("x =",x)
for i in x:
    for n in i:
        if n == 'a':
            c = c + 1
print("Counts:",c)       
