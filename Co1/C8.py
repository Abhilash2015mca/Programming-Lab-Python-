#Get a string from an input string where all occurrences of first character replaced with
#‘$’, except first character.
def change_char(str1):
  char = str1[0]
  str1 = str1.replace(char, '$')
  str1 = char + str1[1:]

  return str1
a = str(input("Enter the String = "))
print(change_char(a)) 