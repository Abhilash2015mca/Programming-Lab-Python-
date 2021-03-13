def search(list,n): 
  
    for i in range(len(list)): 
        if list[i] == n: 
            return True
    return False
  

list = [1, 2, 5, 4,9, 6] 
  

n = 10
  
if search(list, n): 
    print("present") 
else: 
    print("Not Found")