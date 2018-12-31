class complex:
   def __init__(self, real, imag):
      self.re=real
      self.im=imag
   def setRe(self,x):
      self.re = x
      return True
   def setIm(self,x):
      self.im = x
      return True
   def setDesc(self,x):
      self.desc = x
      return True
   def getRe(self):
      return self.re
   def getIm(self):
      return self.im
   def getDesc(self):
      return self.desc
   def dispStr(self):
      return str(self.re) + 'i+ ' + str(self.im)
   def __add__(self, other):
      return complex(self.re+other.re, self.im+other.im)
   def __mul__(self,other):
      return complex(self.re*other.re-self.im*other.im, self.im*other.re+self.re*other.im)

a = complex(1,1)
b = complex(2,2)
c = a+b
print((a*b).dispStr())
a.setDesc("this is complex number representing something important")
b.setDesc("this is irrelevant")
print(a.getDesc())
