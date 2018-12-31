def condense(list):
   condList = []
   if list == [1]:
      return [1]
   else:
      for i in range(0, len(list)-1, 1):
         condList += [list[i] + list[i+1]]
         #print(condList)
   return condList
#print(condense[1, 4, 6, 4, 1])


def pascalTriangle(n):
   if n == 1:
      return [1]
   elif n == 2:
      return [1, 1]
   else:
      return [1] + condense(pascalTriangle(n-1)) + [1]

#print(pascalTriangle(3))