"""
 Array balance point.
 Find, if possible, an index in the array such that the sum of all integers to left of the index is equal to the sum of all the integers right of the index. e.g.
 
balancePoint([5, 4, 0, 19, 3, 4, 2, 0]) = 3
balancePoint([5, 4, 2, 1]) = -1
 
and estimate complexity for solution.
"""

def find_balanced_point_brute(array_int):
    for i in range(1,len(array_int)-1):
        balance_point = i
        sum_left = 0
        sum_right = 0
        for j in range(0, len(array_int)):
            if j < balance_point:
                sum_left += array_int[j]
            elif j > balance_point:
                sum_right += array_int[j]
                if  sum_left < sum_right:
                    break
            if sum_right == sum_left:
                return balance_point
    return -1

def find_balanced_point(array_int):
    sum_all = sum(array_int)
    sum_left = 0
    for i in range(1, len(array_int) - 1):
        sum_left +=array_int[i-1]
        if sum_left == sum_all - sum_left - array_int[i]:
            return i
    return -1

array_int_d = [5, 4, 0, 19, 3, 4, 2, 0]
array_int = [5, 4, 2, 1]
print(find_balanced_point(array_int_d))
print(find_balanced_point(array_int))