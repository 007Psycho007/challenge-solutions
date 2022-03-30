"""
Write a function that accepts a square matrix (N x N 2D array) and returns the determinant of the matrix.

How to take the determinant of a matrix -- it is simplest to start with the smallest cases:

A 1x1 matrix |a| has determinant a.

A 2x2 matrix [ [a, b], [c, d] ] or

|a  b|
|c  d|
has determinant: a*d - b*c.

The determinant of an n x n sized matrix is calculated by reducing the problem to the calculation of the determinants of n matrices ofn-1 x n-1 size.

For the 3x3 case, [ [a, b, c], [d, e, f], [g, h, i] ] or

|a b c|  
|d e f|  
|g h i|  
the determinant is: a * det(a_minor) - b * det(b_minor) + c * det(c_minor) where det(a_minor) refers to taking the determinant of the 2x2 matrix created by crossing out the row and column in which the element a occurs:

|- - -|
|- e f|
|- h i|  
Note the alternation of signs.

The determinant of larger matrices are calculated analogously, e.g. if M is a 4x4 matrix with first row [a, b, c, d], then:

det(M) = a * det(a_minor) - b * det(b_minor) + c * det(c_minor) - d * det(d_minor)
"""
import numpy as np

def determinant(m):
    # Lambda Function to create the cofactor of a an matrix
    cofactor = lambda x,y: np.delete(np.delete(x,0,0),y,1)
    m = np.array(m)
    # Basecase for 1x1 matrix
    if m.shape == (1,1):
        return m[0]
    # Basecase for 2x2 Matrix
    if m.shape == (2,2):
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]
    # Recursive Function to reduce the matrix to a 2x2 basecase
    if m.shape[0] == m.shape[1]:
        result = 0
        for i in range(m.shape[0]):
            if i % 2 == 0:
                result = result + m[0][i] * determinant(cofactor(m,i))
            else:
                result = result - m[0][i] * determinant(cofactor(m,i))
    else:
        result = "Matrix is not equal"
    return result
if __name__ == "__main__":
    m1 = [ [1, 3], [2,5]]
    m2 = [ [2, 5, 3], 
           [1,-2,-1], 
           [1, 3, 4]]
    print(det(m2))
