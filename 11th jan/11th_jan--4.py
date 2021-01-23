numbers = (4,5,6,7,8,0,11,2,4,6,4,2,1,444,5,6,455,554,5574,8,681) 
count_odd = 0
count_even = 0
for x in numbers:
        if not x % 2:
    	     count_even+=1
        else:
    	     count_odd+=1
print("Number of even numbers :",count_even)
print("Number of odd numbers :",count_odd)