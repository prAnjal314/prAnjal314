import numpy as np

# Input Matrix
A = [[3, -5, 6, 4, 7, 45], [2, 3, 9, -1, 4, 1], [5, 8, 1, 4, 2, 67], [1, 3 ,0, 7, 6, 69], [4, 1, 4, 6, 2, 34], [45, 76, 97, 17, 23, 54]]

# Define the function to calculate the determinant of the matrix
def det(mat):
	# Check whether it is a square matrix
	
	if len(mat) == len(mat[0]):
		n = len(mat)
	else:
		return "operation invalid"
	
	if n == 2:		# when order of the matrix is 2
		val = mat[0][0]*mat[1][1] - mat[0][1]*mat[1][0]
		return val
	
	else:			# When the order of the matrix is greater than 2
		val = 0
		for i in range(n):
			tmp = mat
			tmp = tmp[1:]

			for j in range(len(tmp)):
				tmp[j] = tmp[j][0:i] + tmp[j][i+1:]

			val += mat[0][i] * (-1)**(i) * det(tmp)		# Recursion
		return val

print(det(A))
