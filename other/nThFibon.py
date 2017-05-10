def Fibonachi1(n):
    n_prev,n_prev_prev=1,1
    for i in range(2,n):
        n_prev_prev,n_prev= n_prev,n_prev + n_prev_prev
    return n_prev

def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:            
            memo[x] = f(x)
        return memo[x]
    return helper
    
@memoize
def fib(n):
    if n<0:
        raise ValueError("Wrong number")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print (fib(-1))   