from random import  randint
# Python program for counting sort
from _collections import defaultdict
 
def solution(unsorted_prices,max_price):
   
    output = [0 for x in range(max_price+1)]
    # list of 0s at indices 0 to max_price
    prices_to_counts = [0 for x in range(max_price+1)]
    
    # populate prices
    for price in unsorted_prices:
        prices_to_counts[price] +=1
        
    for i in range(max_price+1):
        prices_to_counts[i] += prices_to_counts[i-1]
        
     # Build the output character array
    for i in range(len(unsorted_prices)):
        output[prices_to_counts[arr[i]]-1] = arr[i]
        prices_to_counts[arr[i]] -= 1
                
    return unsorted_prices 

#def my_solution(arr,max_range):
# Driver program to test above function
arr=[]
for x in range(10):
    value = randint(0,20)
    arr.append(value)   
print arr
solution(arr,21)
print arr
#print "Sorted character array is %s"  %("".join(ans))
 