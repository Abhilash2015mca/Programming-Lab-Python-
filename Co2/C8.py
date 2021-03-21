#Accept a list of words and return length of longest word.
list=[]
n=int(input("Enter the number of words = "))
print("Enter words = ")
for i in range(n):
    list.append(len(input()))
print("The longest word has size "+str(max(list)))