def shell_sort(arr):
    #a small modification on insertion sort
    len_arr = len(arr)
    h = 1;
    while (h < len_arr/3):
        h = 3*h + 1
    while h>=1:
        for i in range(h,len_arr):
        #Insert a[i] among a[i-h], a[i-2*h], a[i-3*h]..
            j=i
            while j>=h and arr[j]<arr[j-h]:
                #make exchange while i is on proper place 
                arr[j],arr[j-h] = arr[j-h], arr[j]
                j-=h
        h=h/3
    return arr 

arr = [45,67,23,45,21,24,7,2,6,4,90]
shell_sort(arr)
