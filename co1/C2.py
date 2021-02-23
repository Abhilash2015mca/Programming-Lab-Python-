#display future leap year From current year to a final year entered by user
from datetime import date
today = date.today()
current_year = today.year
input_year = int(input("enter the year :  "))
if (current_year > input_year):
  print("invalid_entry")  
else:
    print("Leap year are :")
    input_year = input_year + 1
    for x in range(current_year, input_year):
         if  x % 100 == 00:
             if x % 400 == 0 :
                 print(x) 
         else:
              if x % 4 == 0:
                 print(x) 
print(x%100)                            
                              