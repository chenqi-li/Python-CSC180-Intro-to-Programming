class uniprogram:
   def __init__(self, fname, lname, stuno, courses, grade, tufee, paid):
      self.firna = fname
      self.lasna = lname
      self.sno = stuno
      self.cour = courses
      self.grad = grade
      self.tf = tufee
      self.p = paid
   def getName(self):
      return str(self.firna) + " " + str(self.lasna)
   def getCourseGrade(self):
      for i in range(0, len(self.grad), 1):
         print("The grade for " + str(self.cour[i]) + " is " + str(self.grad[i]))
   def getTuition(self):
      if self.p == True:
         return "The student's tuition amount is " + str(self.tf) + ". The tuition fee is paid."
      elif self.p == False:
         return "The student's tuition amount is " + str(self.tf) + ". The tuition fee is not paid."

#student1 = uniprogram('Li', 'Chenqi', '1004481940', ['MAT', 'ESC', "PRA"], ['90', '40', '50'], '10', False)
print(student1.getTuition())