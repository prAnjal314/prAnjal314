import numpy as np

A = [[1],
    [3],
    [4]]
B = [[1, 2, 3]]

#a1 = np.array([[1, 2, 1], [3, 4, 3]])
#b1 = np.array([[1, 2], [3, 4], [5, 6]])

def multiply_matrices(a, b):
    if len(a[0]) == len(b):
        l = 0
        c = [[0 for i in range(len(b[0]))] for j in range(len(a))]

        for i in range(len(a)):
            for j in range(len(b[0])):
                sum = 0
                for k in range(len(b)):
                    sum += a[l][k] * b[k][j]
                c[i][j] += sum
            l += 1
        return c
    else:
        return 'operation invalid'

print(multiply_matrices(A, B))
#print(np.dot(a1, b1))