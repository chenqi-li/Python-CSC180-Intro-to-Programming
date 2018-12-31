def seqsum(N):
   cnt = 0
   sum = 0
   while cnt <= N:
      sum = sum + cnt
      cnt += 1
   return sum


N = int(input("Number: "))
print(seqsum(N))