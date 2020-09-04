import sys 

def _merge(a, lo, mid, hi, aux):
    n = hi - lo
    i = lo
    j = mid
    for k in range(n):
        if i == mid:      aux[k] = a[j]; j +=1
        elif j == hi:     aux[k] = a[i]; i +=1
        elif a[j] < a[i]: aux[k] = a[j]; j +=1
        else:             aux[k] = a[i]; i +=1
    a[lo:hi] = aux[0:n]

def _sort(a, lo, hi, aux):
    n = hi - lo
    if n <= 1: return
    
    mid = (lo + hi) // 2
    _sort(a, lo, mid, aux)
    _sort(a, mid, hi, aux)
    _merge(a, lo, mid, hi, aux)
    
def sort(a):
    n = len(a)
    aux = [0 for x in range(0,n)]
    _sort(a, 0, n, aux)
            