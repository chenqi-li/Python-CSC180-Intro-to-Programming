def Palindromize(word):
   cnt = len(word)-2
   new_word = word
   while cnt > -1:
      new_word += word[cnt]
      cnt -= 1
   return new_word

word = input("Word: ")
print(Palindromize(word))
