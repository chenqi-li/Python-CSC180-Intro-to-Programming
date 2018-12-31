
import random

class conway:
   def __init__(self, n1, n2, num_type):
      self.n1 = n1
      self.n2 = n2
      accum0 = []
      store = []
      if num_type == 'zeros':
         for i in range(0, n2, 1):
            accum0 += [0]
         for i in range(0, n1, 1):
            store += [accum0]
      elif num_type == 'random':
         for i in range(0, n1+1, 1):
            store += [accum0]
            accum0 = []
            for i in range(0, n2, 1):
               accum0 += [random.randint(0,1)]
         store = store[1:]
      self.store = store

   def getDisp(self):
      storeStr = ''
      for i in self.store:
         #print('Outside lists:', i)
         for j in i:
            #print('Inside integers:', j)
            if j == 0:
               storeStr += ' '
            elif j == 1:
               storeStr += '*'
         storeStr = storeStr + '\n'
      self.storeStr = storeStr
      return self.storeStr

   def printDisp(self):
      print(self.storeStr)
      return True

   def setPos(self,row,col,val):
      try:
         if val == 1 or val == 0:
            self.store[row][col] = val
            #print('Row: ', row)
            #print('Col: ', col)
         else:
            print('Please input value 0 or 1, NO EXCEPTIONS')
      except:
         print('Row must be between 0 and 9, Column must be between 0 and 11')
      return True

   def getNeighbours(self, row, col):
      #ul t0 ur
      #l0  X r0
      #bl b0 br
      ulr = row - 1
      ulc = col - 1
      t0r = row - 1
      t0c = col
      urr = row - 1
      urc = col + 1
      l0r = row
      l0c = col - 1
      r0r = row
      r0c = col + 1
      blr = row + 1
      blc = col - 1
      b0r = row + 1
      b0c = col
      brr = row + 1
      brc = col + 1


      rows = [ulr, t0r, urr, l0r, r0r, blr, b0r, brr]
      cols = [ulc, t0c, urc, l0c, r0c, blc, b0c, brc]

      cntr = 0
      for x in rows:
         if x == -1:
            rows[cntr] = self.n1-1
         elif x == self.n1:
            rows[cntr] = 0
         cntr += 1

      cntc = 0
      for y in cols:
         if y == -1:
            cols[cntc] = self.n2-1
         elif y == self.n2:
            cols[cntc] = 0
         cntc += 1

      #Reassign values
      ulr = rows[0]
      t0r = rows[1]
      urr = rows[2]
      l0r = rows[3]
      r0r = rows[4]
      blr = rows[5]
      b0r = rows[6]
      brr = rows[7]

      ulc = cols[0]
      t0c = cols[1]
      urc = cols[2]
      l0c = cols[3]
      r0c = cols[4]
      blc = cols[5]
      b0c = cols[6]
      brc = cols[7]



      upperLeft = self.store[ulr][ulc]
      top = self.store[t0r][t0c]
      upperRight = self.store[urr][urc]
      left = self.store[l0r][l0c]
      right = self.store[r0r][r0c]
      bottomLeft = self.store[blr][blc]
      bottom = self.store[b0r][b0c]
      bottomRight = self.store[brr][brc]

      neighbors = [upperLeft, top, upperRight, left, right, bottomLeft, bottom, bottomRight]
      #print(neighbors)
      return neighbors
