
def exchange(a, i, j):
    a[i], a[j] = a[j], a[i]
    
def insertion_sort(a):
    n = len(a)
    for i in range(1, n):
        j = i
        while (j > 0) and (a[j] < a[j-1]):
            exchange(a, j, j-1)
            j -= 1


array_int = [54,26,93,17,77,31,44,55,20]
insertion_sort(array_int)
print(array_int)