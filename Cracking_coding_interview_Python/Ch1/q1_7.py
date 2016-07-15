'''
Given an image represented by NxN matrix, where each pixel in the image is 4 bytes write a method to rotate
the image by 90 degrees. Can you do this in place?
'''
import math

def rotate_matrix_cw90(matrix):
    if (len(matrix) == 0) or (len(matrix) != len(matrix[0])):
        return
    n = len(matrix)
    for layer in range(0,int(n/2)):
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

            
matrix= [[1,1,1,1],[2,2,2,2],[3,3,3,3],[4,4,4,4]]
print(matrix)
rotate_matrix_cw90(matrix)
#print(matrix)