# Form a list of vowels selected from a given word
word = input("enter the word : ")
a = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
vowels_list = []
for x in word :
    if(x in a):
        vowels_list.append(x)
print("vowels in the word =",vowels_list)
