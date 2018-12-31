from counterlib import *
x = counter(1000)
y = counter(50)

x.evolve(10000)
y.evolve(1)
print("The expected value for x is 11000, the actual value is", x.getState())
print("the expected value for y is 51, the actual value is", y.getState())
