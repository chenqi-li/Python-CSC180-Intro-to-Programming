def expo(a,b):
   if b == 0:
      return 1
   elif a == 0:
      return 0
   else:
      return a*expo(a,b-1)

a = int(input("Base: "))
b = int(input("Exponent: "))
print(expo(a,b))