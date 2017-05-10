# Python program for counting sort
from _collections import defaultdict
 
def solution(unsorted_prices,max_price):
    
    # list of 0s at indices 0 to max_price
    prices_to_counts = defaultdict(int)
    
    # populate prices
    for price in unsorted_prices:
        prices_to_counts[ord(price)] +=1
        
    # For each price in prices_to_counts
    k=0
    for price,count in prices_to_counts.items():
        
            # for the number of times the element occurs
        for time in range(count):
            
            # add it to the sorted price list
            unsorted_prices[k]=chr(price)
            k+=1
                
    return unsorted_prices 

#def my_solution(arr,max_range):
# Driver program to test above function
arr = ['b','a','a','s']
#ans = countSort(arr,256)
#ans = solution(arr,256)
ans=solution(arr,9)
print ans
#print "Sorted character array is %s"  %("".join(ans))
 