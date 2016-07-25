'''
Given an image represented by NxN matrix, where each pixel in
the image is 4 bytes write a method to rotate
the image by 90 degrees. Can you do this in place?
'''
from copy import deepcopy
def rotate_matrix_cw90(matrix):
    if len(matrix) == 0 or len(matrix) != len(matrix[0]):
        return
    n = len(matrix)
    for layer in range(0, int(n/2)):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            offset = i - first
            #save top
            top = matrix[first][i]
            #left ->top
            matrix[first][i] = matrix[last - offset][first]
            # bottom -> left
            matrix[last - offset][first] = matrix[last][last - offset]
            #right -> bottom
            matrix[last][last - offset] = matrix[i][last]
            #top -> right
            matrix[i][last] = top
#not in-place
def rotate_matrix_with_deepcopy(matrix, n):
    res = deepcopy(matrix)
    for x in range(0, n):
        for y in range(n-1, -1, -1):
            res[x][n-y-1] = matrix[y][x]
    return res

matrix = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]
print(str(matrix))
print(rotate_matrix_with_deepcopy(matrix, 4))
rotate_matrix_cw90(matrix)
print(matrix)
