from random import  randint
# Python program for counting sort
from _collections import defaultdict
 
def solution(unsorted_prices,max_price):
    
    # list of 0s at indices 0 to max_price
    prices_to_counts = [0 for x in range(max_price+1)]
    
    # populate prices
    for price in unsorted_prices:
        prices_to_counts[price] +=1
        
    # For each price in prices_to_counts
    k=0
    for price,count in enumerate(prices_to_counts):
        
            # for the number of times the element occurs
        for time in range(count):
            
            # add it to the sorted price list
            unsorted_prices[k]=price
            k+=1
                
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
 