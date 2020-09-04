
def binary_search2(arr,ele):
    len_arr = len(arr)
    #Base case 
    if len_arr == 0:
        return False
    
        
    middle = int(len_arr/2)
    if arr[middle]==ele:
        return True
    else:
        if arr[middle]>ele:
            return binary_search(arr[:middle],ele)
        else:
            return binary_search(arr[middle+1:],ele)
        
#interative
def binary_search(arr,ele):
    first = 0
    len_arr = len(arr)
    last = len_arr - 1
    if len_arr == 0:
        return False
    
    while first <= last and first > -1 and last < len_arr:
        middle = int((first + (last - first)/2))
        if arr[middle]==ele:
            return True
        else:
            if arr[middle]>ele:
                last = middle-1
            else:
                first = middle + 1
    return False
arr = [1,2,3,4,5,6,7,8,9,10]
binary_search(arr,4)
binary_search2(arr,2.2)
