'''
Write an algorithm such that if an element in an MxN matrix is 0, it's entire
row and column are set to 0.
'''

col_dict = {}

def nullify_column(matrix):
    for column in col_dict:
        for row in matrix:
            row[column] = 0

            
def set_sero(matrix):
    #set 0 in col
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                col_dict[j] = True
    #set 0 in row
    for i in range(len(matrix)):
        if 0 in matrix[i]:
                matrix[i] = [0 for index in range(len(matrix))]
    

    nullify_column(matrix)        
    
matrix = [[1,0,3,5], 
          [2,5,6,2], 
          [9,3,0,8], 
          [3,4,5,7], 
          [0,8,3,1]]
print(matrix)
set_sero(matrix)
print(matrix)