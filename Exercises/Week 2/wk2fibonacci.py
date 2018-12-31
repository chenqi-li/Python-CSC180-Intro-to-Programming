def fibonacci(n):
   if n <= 2:
      return 1
   else:
      return (fibonacci(n-2) + fibonacci(n-1))

def fibonacciseq(n):
   x = 1
   fibonacciseq = []
   while x < n+1:
      fibonacciseq += [fibonacci(x)]
      x += 1
   return fibonacciseq

def fibonacciSum(n):
   seqToSum = list(fibonacciseq(n))
   sum = 0
   for num in seqToSum:
      sum += num
   return sum

print(fibonacciseq(8))
print(fibonacciSum(8))