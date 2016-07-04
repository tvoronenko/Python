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

