import numpy

x = numpy.array([[1, 2], [3, 4]])
y = numpy.array([[5, 6], [7, 8]])

print(" The matrix X :", x)
print(" The matrix Y :", y)

# Addition of Matrix X and Y

print(" The Addition of matrix X & Y :", numpy.add(x, y))

# Subtraction of Matrix X and Y

print(" The Substraction of matrix X & Y :", numpy.subtract(x, y))

# multiplication of Matrix X and Y

print(" Multiplication of matrix X & Y :", numpy.multiply(x, y))

# Transpose of matrix X

print(" Transpose of matrix X :", (x.T))

# Transpose of matrix Y

print(" Transpose of matrix Y :", (y.T))
