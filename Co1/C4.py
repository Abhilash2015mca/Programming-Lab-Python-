#count the occurences of each word in a line of text
sentence = input("enter the text = ")
words = sentence.split(' ')
count = {}
for word in words:                                                                                                                                                                                              
    count[word] = count.get(word, 0) + 1   
print(count)        
