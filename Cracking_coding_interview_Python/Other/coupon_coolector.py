import random
import sys
"""
Created 

"""
n = int(sys.argv[1])
count = 0
collected_count = 0 
is_collected = [False for x in range(0,n)]

while collected_count < n:
    value = random.randrange(0,n)
    count += 1
    if not is_collected[value]:
        collected_count +=1
        is_collected[value] = True
        
print(count)
    