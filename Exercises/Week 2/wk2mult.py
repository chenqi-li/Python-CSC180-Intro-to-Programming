def neg(c):
   return -c
def mult(a,b):
   if a < 0:
      a = abs(a)
      negative = True
      #print("a is negative")
   else:
      negative = False

   if a == 0:
      return 0
   elif a == 1 and negative == True:
      return -b
   elif a == 1 and negative == False:
      return b
   else:
      return neg(b + mult(a-1,b))

a = int(input("Num 1: "))
b = int(input("Num 2: "))
print(mult(a, b))