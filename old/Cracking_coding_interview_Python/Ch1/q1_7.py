'''
Given an image represented by NxN matrix, where each pixel in
the image is 4 bytes write a method to rotate
the image by 90 degrees. Can you do this in place?
'''
from copy import deepcopy
def rotate_matrix_cw90(matrix):
    if len(matrix) == 0 or len(matrix) != len(matrix[0]):
        return
    matrix_size = len(matrix)
    for layer in range(0, int(matrix_size/2)):
        first = layer
        last = matrix_size - 1 - layer
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
def rotate_matrix_with_deepcopy(matrix, matrix_size):
    res = deepcopy(matrix)
    for i in range(0, matrix_size):
        for j in range(matrix_size-1, -1, -1):
            res[i][matrix_size-j-1] = matrix[j][i]
    return res

def main():
    """test"""
    matrix = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]
    print(str(matrix))
    print(rotate_matrix_with_deepcopy(matrix, 4))
    rotate_matrix_cw90(matrix)
    print(matrix)

if __name__ == '__main__':
    main()
