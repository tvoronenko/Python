from math import sqrt
from bitarray import bitarray
def generate_prime(n):

    if n<=1:
        return None
    output = [True for x in range(n+1)]
    output[0] = output[1] = False
    _sqrt = int(sqrt(n)+1)
    for i in range(2,_sqrt):
        if output[i]:
            k=i*i
            while k <=n:
                output[k] = False
                k+=i
   
    output = [i  for i,x in enumerate(output) if x==True]
    return output

def is_prime(n):
    if n<=1:
        return False
    _sqrt = int(sqrt(n)+1)
    for i in range(2,_sqrt):
        if n%i==0:
            return False
    return True

print(generate_prime(20)) 
print(is_prime(20))
print(is_prime(13))
n=50
_sqrt = int(sqrt(n)+1)
non_prime = [j  for j in range(i*i,n+1,i) for i in range(2,_sqrt)]
print  non_prime