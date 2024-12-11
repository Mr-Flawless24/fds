import numpy

x = numpy.array([[1,2],[3,4]])
y = numpy.array([[5,6],[7,8]])

for i in range(len(x)):
    for j in range(len(x[0])):
        print(x[i][j],end ="  ")

    print()

for i in range(len(y)):
    for j in range(len(y[0])):
        print(y[i][j],end ="  ")

    print()

print("Addition of matrices")
for i in range(len(x)):
    for j in range(len(y)):
        print(x[i][j]+y[i][j],end = " ")
    print()

print("substraction of matrices")
for i in range(len(x)):
    for j in range(len(y)):
        print(x[i][j]-y[i][j],end = " ")
    print()

print("multiplication of matrices")
for i in range(len(x)):
    for j in range(len(y)):
        print(x[i][j]*y[i][j],end = " ")
    print()

print("transpose of matrix X")
transA = [[0,0],
         [0,0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        transA[j][i] = x[i][j]
    print(transA)

print("transpose of matrix Y")
transA = [[0,0],
         [0,0]]
for i in range(len(y)):
    for j in range(len(y[0])):
        transA[j][i] = x[i][j]
    print(transA)