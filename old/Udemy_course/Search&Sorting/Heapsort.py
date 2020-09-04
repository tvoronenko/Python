from random import  randint
#build the heap in array - largest is root
def heapify(a, size):
    #latest element i, let's find its parent
    end= size -1
    parent = int((end - 1)//2)
    
    while parent >=0:
        
        sift_down(a,parent,size - 1)
        parent = parent - 1
def max_child(a,i,size):
    if (2*i+2)> size:
        return (2*i+1)
    else:
        if a[2*i+2]>a[2*i+1]:
            return (2*i+2)
        else:
            return (2*i+1)
        
def sift_down(a, start, end):
    root = start
    
    while (2*root + 1) <=end:
        mc = max_child(a,root,end)
        if a[root]< a[mc]:
            a[root],a[mc] = a[mc], a[root]
        root = mc

def heapsort(a):
    n=len(a)
    heapify(arr,n)
    print(arr)
     # One by one extract elements
    end = n-1
    while end >0:
        #move max to end and reheap array
        arr[end], arr[0] = arr[0], arr[end]
        end = end - 1
        sift_down(arr, 0,end)

arr=[]
for x in range(10):
    value = randint(0,20)
    arr.append(value)   
#arr = [x for x in range(100)]
#arr=[1,2,3,7,5,6,7,8,9,10]
print(arr)
heapsort(arr)
print(arr)