def fact(x):
   #print("Argument is " + str(x))
   if x <= 1:
      return 1
   else:
      return x*fact(x-1)

x = int(input("Number: "))
print(fact(x))