def expo(a,b):
   ans = 1
   if b == 0:
      return 1
   for i in range(0, b, 1):
      ans *= a
   return ans

#print(expo(2, 5))

def fibo(n):
   ans = 0
   a = 1
   b = 1
   if n == 1 or n == 2:
      return 1

   else:
      for i in range(0, n-2, 1):
         ans = a + b
         a = b
         b = ans
      return ans

#print(fibo(14))

def condense(list):
   condList = []
   if list == [1]:
      return [1]
   else:
      for i in range(0, len(list)-1, 1):
         condList += [list[i] + list[i+1]]
         #print(condList)
   return condList

def pasc(n):
   seq = []
   if n <= 1:
      return [1]
   elif n == 2:
      return [1, 1]
   else:
      for i in range(0, n-1, 1):
         seq = [1] + condense(seq) + [1]
      return seq

def condenseT(list):
   condList = []
   #print(len(list))
   if list == [1]:
      return [1]
   elif list == [1, 1, 1]:
      return [1, 2, 3, 2, 1]
   else:
      for i in range(1, len(list)-1, 1):
         condList += [list[i-1] + list[i] + list[i+1]]
         print(condList)
      condList = [1] + [list[0]+list[1]] + condList + [list[len(list)-2] + list[len(list)-1]] + [1]
   return condList
#print(condenseT([1, 2, 3, 2, 1]))


def tPasc(n):
   seq = [1, 1, 1]
   if n <= 1:
      return [1]
   elif n == 2:
      return [1, 1, 1]
   else:
      for i in range(0, n-2, 1):
         seq = condenseT(seq)
      return seq
#print(tPasc(5))

def condenseBT(list):
   condList = []
   if list == [1]:
      return [1,2]
   elif list == [1,2]:
      return [1, 3, 4]
   else:
      for i in range(0, len(list)-1, 1):
         condList += [list[i]+list[i+1]]

   return [1] + condList + [2*list[len(list)-1]]

#print(condenseBT([1, 4, 7, 8]))

def bernoulliTriangle(n):
   seq = [1, 2]
   if n == 1:
      return [1]
   elif n == 2:
      return [1, 2]
   else:
      for i in range(0, n-2, 1):
         seq = condenseBT(seq)
      return seq

print(bernoulliTriangle())