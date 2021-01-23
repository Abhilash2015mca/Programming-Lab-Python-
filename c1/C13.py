#Create a list of colors from comma-separated color names entered by user. Display first and last colors
lst = []
for x in range(0,4):
    colour = input("enter the colour = ")
    lst.append(colour)
print( lst[0], lst[-1] ) 