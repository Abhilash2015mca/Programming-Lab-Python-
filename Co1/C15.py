#Print out all colors from color-list1 not contained in color-list2.
list1=["blue","red","green","yellow"]
list2=["yellow","red","cyan"]
print([item for item in list1 if item not in list2])