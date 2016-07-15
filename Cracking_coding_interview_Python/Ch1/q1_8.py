'''
Write an algorithm such that if an element in an MxN matrix is 0, it's entire
row and column are set to 0.
'''
row_dict = {}
col_dict = {}

def nullify_column(matrix):
    for column in col_dict:
        for row in matrix:
            row[column] = 0


def nullify_row(matrix):
    for row in row_dict:
        for index in range(0, len(matrix[0])):
            matrix[row][index] = 0
            
def set_sero(matrix):
    print
    
matrix = [[1,0,3,5], [2,5,6,2], [9,3,0,8], [3,4,5,7], [0,8,3,1]]

print(set_sero(matrix))