def LeibnizAcc(n):
   cnt = 3
   posneg = -1
   rHs = 0
   pi = (rHs + 1)*4
   while abs(pi - 3.1415926535897932384626) > n:
      #print(posneg)
      #print(rHs)
      #print(cnt)
      rHs += posneg*(1/cnt)
      cnt += 2
      posneg *= -1
      pi = (rHs + 1)*4
   return cnt

n = float(input("Number: "))
print(LeibnizAcc(n))