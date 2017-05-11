# Merges two subarrays of arr[].
# First subarray is arr[l..m]
# Second subarray is arr[m+1..r]
from random import  randint
      
def merge_sort(arr):
    n= len(arr)
    aux = [0 for x in range(n)]
    _sorting(arr,0,n,aux)

def _sorting(arr,low, high, aux):
    if (high-low) >1:
        middle = low + (high - low)//2
        _sorting(arr,low, middle, aux)
        _sorting(arr,middle, high, aux)
        
        if arr[middle-1]>arr[middle]:
            print "Merge"
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

arr=[]
for x in range(10):
    value = randint(0,20)
    arr.append(value)   
#arr = [x for x in range(100)]
arr=[1,2,3,7,5,6,7,8,9,10]
print arr
merge_sort(arr)
print arr

