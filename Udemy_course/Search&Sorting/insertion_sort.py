def insertion_sort(arr):
    len_arr = len(arr)
    for i in range(1,len_arr):
        #Insert a[i] among a[i-1], a[i-2], a[i-3]....
        j=i
        while j>0 and arr[j]<arr[j-1]:
            #make exchange while i is on proper place 
            arr[j],arr[j-1] = arr[j-1], arr[j]
            j-=1
    return arr 


arr =[3,5,4,6,8,1,2,12,41,25]
insertion_sort(arr)

