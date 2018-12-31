class vec2:
   def __init__(self, x, y):
      self.dim0 = x
      self.dim1 = y

   def __add__(self, other):
      return vec2(self.dim0 + other.dim0, self.dim1 + other.dim1)


   def __mul__(self, other):
      return self.dim0 * other.dim0 + self.dim1 * other.dim1


   def getStr(self):
      return str(self.dim0), str(self.dim1)


   def getX(self):
      return self.dim0


   def setX(self, x):
      self.dim0 = x
      return True

x=vec2(1,2)
y=vec2(3,4)
z=x+y
dotprod=x*y
print(z.getStr())
z.setX(5)


sTr='12345'
sTr = sTr[1:3]
print(sTr)