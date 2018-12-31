def reducingSum(a, b):
   return a + b

def reduce(x, y):
   sum = 0
   if len(y) % 2 == 0:
      for i in range(0, len(y), 2):
         sum += reducingSum(y[i], y[i+1])
      return sum
   elif len(y) % 2 == 1:
      sum += y[0]
      for i in range(1, len(y), 2):
         sum += reducingSum(y[i], y[i+1])
      return sum

print(reduce(reducingSum, [1, 2, 3, 4, 5, 6, 7]))





def reducingProduct(a, b):
   return a * b

def reduce(x, y):
   product = 1
   if len(y) % 2 == 0:
      for i in range(0, len(y), 2):
         product *= reducingProduct(y[i], y[i+1])
      return product
   elif len(y) % 2 == 1:
      product *= y[0]
      for i in range(1, len(y), 2):
         product *= reducingProduct(y[i], y[i+1])
      return product

print(reduce(reducingProduct, [1, 2, 3, 4, 5, 6, 7]))
