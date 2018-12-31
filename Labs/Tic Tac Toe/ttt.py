from tttlib import *

T = genBoard()
print('Welcome to python3 TicTacToe! Note: only integers are allowed! Otherwise, restart the game!')

while True:
   printBoard(T)
   moveX = input("X move?")


   if moveX != '0' and moveX != '1' and moveX != '2' and moveX != '3' and moveX != '4' and moveX != '5' and moveX != '6' and moveX != '7' and moveX != '8':
      print('Too bad! You did not input an integer between 0 and 8! Restart the game')
      break
   elif int(moveX) == 0 or int(moveX) == 1 or int(moveX) == 2 or int(moveX) == 3 or int(moveX) == 4 or int(moveX) == 5 or int(moveX) == 6 or int(moveX) == 7 or int(moveX) == 8:
      if T[int(moveX)] == 0:
         T[int(moveX)] = 1
      else:
         print('Too bad! It is already occupied! Restart the game!')

   #print(T)
   state = analyzeBoard(T)

   if state == 1:
      print("Player X wins!")
      break
   elif state == 3:
      print("The game is drawn!")
      break
   elif state == -1:
      print('There is an error!')
      break

   printBoard(T)
   moveO = input("O move?")

   if moveO!= '0' and moveO != '1' and moveO != '2' and moveO != '3' and moveO != '4' and moveO != '5' and moveO != '6' and moveO != '7' and moveO != '8':
      print('Too bad! You did not input an integer between 0 and 8! Restart the game!')
      break
   elif int(moveO) == 0 or int(moveO) == 1 or int(moveO) == 2 or int(moveO) == 3 or int(moveO) == 4 or int(moveO) == 5 or int(moveO) == 6 or int(moveO) == 7 or int(moveO) == 8:
      if T[int(moveO)] == 0:
         T[int(moveO)] = 2
      else:
         print('Too bad! It is already occupied! Restart the game!')
         break

   state = analyzeBoard(T)
   if state == 2:
      print("Player O wins!")
      break
   elif state == 3:
      print("The game is drawn!")
      break
   elif state == -1:
      print("There is an error!")
      break
