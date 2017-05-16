from math import sqrt
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
print(generate_prime(20)) 