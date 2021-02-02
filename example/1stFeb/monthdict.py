#Create a dictionary whose keys are month names and whose values are the number of days in corrensponding months.
#Ask the user to enter a month name and use the dictionary to tell them how many days are in the month.
#Print out all of the keys in alphabetical order
#Print out all of the months with 30 days
dict = {}
dict = {'January': 31, 'Febuary': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31, 'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31 }
x = (input("Enter The Month = "))
print("No of Days =", dict[x])
print("Months in Alphabetical Order = ")
sortedkeys = sorted(dict, key=str.lower)
for i in sortedkeys:
    print (i)
print("Months with 30 days = ")
for i in sortedkeys:
    if dict[i] == 30:
        print(i)
