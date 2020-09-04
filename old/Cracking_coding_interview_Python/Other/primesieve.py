import sys
'''
'''
n = int (sys.argv[1])
is_prime = [True for x in range(0,n+1)]
for i in range(2,n):
    if(is_prime[i]):
        for j in range(2, n//i +1):
            is_prime[i*j] = False
count = 0
for i in range (2,n+1):
    if(is_prime[i]):
        count += 1
print(count)