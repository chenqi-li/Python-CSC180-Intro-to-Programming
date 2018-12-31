def genBoard():

   dataBoard = []
   i = 0
   while i < 9:
      #print(i)
      dataBoard = dataBoard + [0]
      #print(dataBoard)
      i = i + 1
   return dataBoard
#print(genBoard())

#genBoard()

#dataBoard = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#print(dataBoard)

#T = [2, 1, 1, 2, 2, 2, 1, 2, 1]

def printBoard(T):
   index = 0
   dispBoard = []
   for x in T:
      if x == 0:
         dispBoard = dispBoard + [index]
      elif x == 1:
         dispBoard = dispBoard + ['X']
      else:
         dispBoard = dispBoard + ['O']
      index += 1
   print(' ' + str(dispBoard[0]) + ' | ' + str(dispBoard[1]) + ' | ' + str(dispBoard[2]))
   print('---|---|---')
   print(' ' + str(dispBoard[3]) + ' | ' + str(dispBoard[4]) + ' | ' + str(dispBoard[5]))
   print('---|---|---')
   print(' ' + str(dispBoard[6]) + ' | ' + str(dispBoard[7]) + ' | ' + str(dispBoard[8]))

   #Error checks
   #If length is not 0
   if len(T) == 9:
      return True
   #if any is not equal to 0 or 1 or 2
   elif T[0] != 0 or T[1] != 0 or T[2] != 0 or T[3] != 0 or T[4] != 0 or T[5] != 0 or T[6] != 0 or T[7] != 0 or T[8] != 0 or T[0] != 1 or T[1] != 1 or T[2] != 1 or T[3] != 1 or T[4] != 1 or T[5] != 1 or T[6] != 1 or T[7] != 1 or T[8] != 1 or T[0] != 2 or T[1] != 2 or T[2] != 2 or T[3] != 2 or T[4] != 2 or T[5] != 2 or T[6] != 2 or T[7] != 2 or T[8] != 2:
      return True
   #if any element is not an integer
   elif type(T[0]) == int or type(T[1]) == int or type(T[2]) == int or type(T[3]) == int or type(T[4]) == int or type(T[5]) == int or type(T[6]) == int or type(T[7]) == int or type(T[8]) == int:
      return True
   else:
      return False

#print(printBoard(T))
#T = [1, 1, 1, 0, 0, 0, 0, 0, 0]

def analyzeBoard(T):

   row1 = T[0:3:1]
   row2 = T[3:6:1]
   row3 = T[6:9:1]
   column1 = T[0:9:3]
   column2 = T[1:9:3]
   column3 = T[2:9:3]
   diagonal1 = [T[2], T[4], T[6]]
   diagonal2 = [T[0], T[4], T[8]]

   winningSituations = [row1, row2, row3, column1, column2, column3, diagonal1, diagonal2]

   result = 0

   while result == 0:
      #Check for winning situations
      for y in winningSituations:
         if y == [1, 1, 1]:
            result = 1
            # print('[1,1,1]' + str(result))
            break
         elif y == [2, 2, 2]:
            result = 2
            # print('[2,2,2]' + str(result))
            break
      if result == 1 or result == 2:
         # print('Result is won')
         break
         # Check for draw
      elif T[0] != 0 and T[1] != 0 and T[2] != 0 and T[3] != 0 and T[4] != 0 and T[5] != 0 and T[6] != 0 and T[
         7] != 0 and T[8] != 0:
         result = 3
         # print('Result is 3')
         break
         # Otherwise board is still in play
      else:
         result = 0
         break

         # Error checks
         # If length is not 0
      if len(T) != 9:
         result = -1

      # if any is not equal to 0 or 1 or 2
   if T[0] != 0 and T[0] != 1 and T[0] != 2:
      result = -1
   elif T[1] != 0 and T[1] != 1 and T[1] != 2:
      result = -1
   elif T[2] != 0 and T[2] != 1 and T[2] != 2:
      result = -1
   elif T[3] != 0 and T[3] != 1 and T[3] != 2:
      result = -1
   elif T[4] != 0 and T[4] != 1 and T[4] != 2:
      result = -1
   elif T[5] != 0 and T[5] != 1 and T[5] != 2:
      result = -1
   elif T[6] != 0 and T[6] != 1 and T[6] != 2:
      result = -1
   elif T[7] != 0 and T[7] != 1 and T[7] != 2:
      result = -1
   elif T[8] != 0 and T[8] != 1 and T[8] != 2:
      result = -1

   #if any element is not an integer
   if type(T[0]) != int or type(T[1]) != int or type(T[2]) != int or type(T[3]) != int or type(T[4]) != int or type(
           T[5]) != int or type(T[6]) != int or type(T[7]) != int or type(T[8]) != int:
      result = -1

      # If number of X and O differ by more than 1
   xCount = 0
   oCount = 0
   for z in T:
      if z == 1:
         xCount += 1
      elif z == 2:
         oCount += 1
   if abs(xCount - oCount) == 1 or abs(xCount - oCount) == 0:
      result == result
   else:
      result = -1

   return result

# print(analyzeBoard(T))
