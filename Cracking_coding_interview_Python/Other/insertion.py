import sys

def exchange(a, i, j):
    a[i], a[j] = a[j], a[i]
    
def sort(a):
    n = len(a)
    for i in range(1, n):
        j = i
        while (j > 0) and (a[j] < a[j-1]):
            exchange(a, i, j-1)
            j -= 1
