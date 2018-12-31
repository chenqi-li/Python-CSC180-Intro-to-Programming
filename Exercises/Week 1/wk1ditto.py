def ditto(N):
   cnt = 0
   sum = 0
   while cnt <= N:
      if cnt % 2 == 0:
         sum -= cnt
         #print('positive' + str(cnt))
      elif cnt % 2 == 1:
         sum += cnt
         #print('positive' + str(cnt))
      cnt += 1
   return sum

N = int(input("Number: "))
print(ditto(N))
