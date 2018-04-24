#A python exercise that is a Pig Latin Translator
# mentions slicing and isalpha(), which checks for numbers in strings

pyg = "ay"
print ("Welcome to the Pig Latin Translator!")
original = input("Enter a word: ")
#You can use .isalpha() to check that a string doesn't contain any non-letter characters!
if len(original) > 0 and original.isalpha():
  word = original.lower()
  first = word[0]
  print (word)
  print (first)
  new_word = word + first + pyg
  #removes the first character from the variable new_world using slice
  new_word = new_word[1:len(new_word)]
  print (new_word)
else:
  print("empty")
# Start coding here!

