word_dict = { 'this': 11, 'at': 9, 'here': 5, 'why': 12, 'is': 2 }

sorted_dict = dict( sorted(word_dict.items(),
                           key=lambda item: item[1],
                           reverse=True))
print('Sorted Dictionary: ')
print(sorted_dict)