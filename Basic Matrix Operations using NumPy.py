import numpy as np

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)


addition = A + B
print("\nMatrix Addition:")
print(addition)


multiplication = np.dot(A, B)
print("\nMatrix Multiplication:")
print(multiplication)

transpose = A.T
print("\nTranspose of Matrix A:")
print(transpose)
