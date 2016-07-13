"""
given array of int. Find  all pairs which gives sum 7;

and estimate complexity for solution
"""
#return result without duplicate because of using set
#return result with additional duplicates if check target in array_int
#O(n(n+n))
def find_sum_of_pair(array_int, sum):
    result = {}
    set_int = set(array_int)
    if array_int == None:
        return
    if len(array_int) < 2:
        return
    for value in array_int:
        target = sum - value
        if (target in set_int) and (target not in result):
            result[value] = target
    
    if len(result) == 0:
        return
    else:
        return result
#O(n)
def find_sum_of_pair1(array_int, sum):
    array_int.sort()
    result = {}
    left = 0
    right = len(array_int) - 1
    while ( left < right):
        internal_sum = array_int[left] + array_int[right]
        if internal_sum == sum:
            result[array_int[left]] = array_int[right]
            left += 1
            right -= 1
        elif internal_sum < sum:
            left += 1
        else:
            right -= 1
    if len(result) == 0:
        return
    else:
        return result
 

array_int_duplic = [2, 4, 8, 5, 6, -2, 4, 7, 0, 9]
array_int = [9, 7, 3, 5, 4, 8, 2 ]
print(find_sum_of_pair(array_int_duplic, 7))
print(find_sum_of_pair(array_int, 7))