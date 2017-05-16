def selection_sort(arr):
    len_arr = len(arr)
    for i in range(len_arr):
        #select i as minimum
        min_i=i
        for j in range(i+1,len_arr):
            if arr[i]>arr[j]:
                #find true minimum
                min_i = j
        if min_i!=i:
            #exchange i with minimum
            arr[i],arr[min_i] = arr[min_i],arr[i]
    return arr

arr = [3,2,13,4,6,5,7,8,1,20]
selection_sort(arr)

