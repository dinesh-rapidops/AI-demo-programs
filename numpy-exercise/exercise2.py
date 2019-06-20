# Multiplication of two columns
import numpy as np

# [1 2 2 2]
A = np.array([1,2,2,2])
print(A)

# [2 4 3 4]
B = np.array([[2,4,3,4],[1,1,1,1]])
print(B)


# [[2 4 3 4]
#  [4 8 6 8]
#  [4 8 6 8]
#  [4 8 6 8]]
C = np.outer(A,B)
print(C)