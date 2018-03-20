from task import Matrix

matrixA = Matrix(2,2,2,2)
matrixB = Matrix(1,0,0,1)

print("Matrix A")
print(matrixA)

print("Matrix B")
print(matrixB)

print("A + B")
print(matrixA + matrixB)

print("A + 1")
print(matrixA + 1)

print("1 + A")
print(1 + matrixA)

print("A * B")
print(matrixA*matrixB)

print("A * 2")
print(matrixA*2)

print("A * 2")
print(2*matrixA)

print("Construct")
print(Matrix.construct(1,2,3,4))
