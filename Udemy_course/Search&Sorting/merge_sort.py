# Merges two subarrays of arr[].
# First subarray is arr[l..m]
# Second subarray is arr[m+1..r]

def merge_sort_inplace(arr):
    n= len(arr)
    _sorting_inplace(arr,0,n)
  
  
def _sorting_inplace(arr,low, high):
    if (high-low) >1:
        middle = low + (high - low)//2
        _sorting_inplace(arr,low, middle)
        _sorting_inplace(arr,middle, high)
        
        _merge_inplace(arr,low, middle,high)
        
def merge_sort(arr):
    n= len(arr)
    aux = [0 for x in range(n)]
    _sorting(arr,0,n,aux)

def _sorting(arr,low, high, aux):
    if (high-low) >1:
        middle = low + (high - low)//2
        _sorting(arr,low, middle, aux)
        _sorting(arr,middle, high, aux)
        
        _merge(arr,low, middle,high,aux)
        
def _merge(arr,low, middle,high,aux):
    n=high-low
    i=low
    j=middle
    for k in range(n):
        if i==middle:
            aux[k] = arr[j]
            j+=1
        elif j==high:
            aux[k] = arr[i]
            i+=1
        elif arr[i]<arr[j]:
            aux[k] = arr[i]
            i+=1
        else:
            aux[k] = arr[j]
            j+=1
            
    arr[low:high]=aux[0:n]

def _merge_inplace(arr,low, middle,high):
    n=high-low
    i=low
    j=middle
    left_el = arr[i]
    right_el = arr[j]
    for k in range(n):
        if i==middle:
            arr[low+k] = right_el
            j+=1
            #check for overflow
            if j <len(arr):
                right_el = arr[j]
        elif j==high:
            arr[low+k] = left_el
            i+=1
            left_el = arr[i]
        elif left_el<right_el:
            temp=arr[low+k]
            arr[low+k] = left_el
            i+=1
            if i==(k+low):
                left_el = temp
            else:
                left_el = arr[i]
        else:
            arr[low+k] = right_el
            j+=1
            #check for overflow
            if j <len(arr):
                right_el = arr[j]
    
arr = [11,2,5,4,7,6,8,1,23]
merge_sort_inplace(arr)
print arr

