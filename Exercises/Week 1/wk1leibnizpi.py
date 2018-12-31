def LeibnizPi(n):
   cnt = 3
   posneg = -1
   rHs = 0
   while cnt <= n:
      #print(posneg)
      #print(rHs)
      #print(cnt)
      rHs += posneg*(1/cnt)
      cnt += 2
      posneg *= -1
   pi = (rHs + 1)*4
   return pi

n = float(input("Number: "))
print(LeibnizPi(n))