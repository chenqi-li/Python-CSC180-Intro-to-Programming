def sum(x):
   if x == []:
      return 0
   elif len(x) == 1:
      return x[0]
   else:
      return x[0] + sum(x[1:])

print(sum([1,2,3,4,5]))