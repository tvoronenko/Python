from random import  randint
# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
def partition(a,low,high):
    i = low -1
    pivot = a[high]
    for j in range(low , high+1):
  
        # If current element is smaller than or
        # equal to pivot
        if   arr[j] <= pivot:
          
            # increment index of smaller element
            i = i+1
            if j>i:
                arr[i],arr[j] = arr[j],arr[i]
  
    return i

# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index
 
# Function to do Quick sort
def quickSort(arr,low,high):
    if low < high:
 
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr,low,high)
 
        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

# Function to do Quick sort
# arr[] --> Array to be sorted,
# l  --> Starting index,
# h  --> Ending index
def quickSortIterative(arr,l,h):
 
    # Create an auxiliary stack
    size = h - l + 1
    stack = [0] * (size)
 
    # initialize top of stack
    top = -1
 
    # push initial values of l and h to stack
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h
 
    # Keep popping from stack while is not empty
    while top >= 0:
 
        # Pop h and l
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1
 
        # Set pivot element at its correct position in
        # sorted array
        p = partition( arr, l, h )
 
        # If there are elements on left side of pivot,
        # then push left side to stack
        if p-1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1
 
        # If there are elements on right side of pivot,
        # then push right side to stack
        if p+1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h

arr=[]
for x in range(10):
    value = randint(0,20)
    arr.append(value)   
#arr = [x for x in range(100)]
#arr=[1,2,3,7,5,6,7,8,9,10]
print arr
quickSort(arr,0,len(arr)-1)
print arr