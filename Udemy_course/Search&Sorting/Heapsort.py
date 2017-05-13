from random import  randint
#build the heap in array - largest is root
def heapify(a, size):
    #latest element i, let's find its parent
    end= size -1
    start = (end - 1)//2
    
    while start >=0:
        sift_down(a,start,size - 1)
        start = start - 1

def sift_down(a, start, end):
    root = start
    i_left = 2*root + 1
    i_right = 2*root + 2
    
    while i_left <=end:
        child =  2*root + 1
        swap = root
        if a[swap] < a[child]:
            swap = child
        if (child +1) <= end and a[swap]<a[child+1]:
            swap = child + 1
        if swap  == root:
            return
        else:
            a[root],a[swap] = a[swap], a[root]
            root=swap
#move up bigger element    
#def move_up(i):
#    if
#move down smaller
#def move_up(a,i,size):
  # # parent = (i-1)//2
  #  while (i > 0 and )
def move_down(a, i,size):
    if (2*i +1)< size:
        if a[i]< a[2*i +1]:
           a[i],a[2*i +1] = a[2*i +1], a[i]
           move_down(a,(2*i +1),size)
arr=[]
for x in range(10):
    value = randint(0,20)
    arr.append(value)   
#arr = [x for x in range(100)]
#arr=[1,2,3,7,5,6,7,8,9,10]
print arr
heapify(arr,len(arr))
print arr