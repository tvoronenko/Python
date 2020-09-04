import sys

def _search(key, a, lo, hi):
    if hi <= lo: return -1
    mid = (lo + hi) // 2
    if a[mid] > key:
        return _search(key, a, lo, mid)
    elif a[mid] < key:
        return _search(key, a, mid+1, hi)
    else:
        return mid
    
def search(key, a):
    return _search(key, a, 0, len(a))

array_int = [5, 4, 0, 19, 3, 4, 2, 0]
print(search(0, array_int))
