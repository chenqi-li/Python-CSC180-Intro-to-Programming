class seqdetector:
   def __init__(self):
      self.list = []
   def evolve(self, word):
      word_list = ['here', 'are', 'the', 'solutions', 'to', 'the', 'next', 'exam']
      self.list = self.list + [word]
      cnt = 0
      for i in self.list:
         #print('self.list before is:', self.list)
         #print('cnt is:', cnt)
         #print('i is:', cnt)
         if self.list[cnt] == word_list[cnt]:
            self.list = self.list
         elif self.list[cnt] != word_list[cnt]:
            self.list = self.list[cnt:]
         cnt += 1
         #print('self.list after is:', self.list)
         #print('\n')
      if self.list == word_list:
         return True
      else:
         return False


#words_list = ['here', 'are', 'the', 'solutions', 'to', 'the', 'next', 'here', 'are', 'the', 'solutions', 'to', 'the', 'next', 'exam']
words_list = ['here', 'are', 'the', 'next', 'exam', ]

def main():
   x = seqdetector()
   n = 0
   for i in words_list:
      status = x.evolve(i)
      if status == True:
         print("Detected: end position is", n)
      n = n + 1
   return True

main()
