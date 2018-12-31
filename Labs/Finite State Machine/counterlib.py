class counter:
   def __init__(self,initCnt):
      self.cnt = initCnt
   def evolve(self,x):
      self.x = x
      self.cnt += self.x
      return True
   def getState(self):
      return self.cnt
   #state(at time n+1) = evolve(getState(), x)