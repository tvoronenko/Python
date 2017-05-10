def solution(lst):
  # Start at index 2 (3rd element) and assign highest and lowest 
    # based off of first two elements
    
    # Highest Number so far
    high = max(lst[0],lst[1])
    
    # Lowest number so far
    low = min(lst[0],lst[1])
    
    # Initiate Highest and lowest products of two numbers
    high_prod2 = lst[0]*lst[1]
    low_prod2 = lst[0]*lst[1]
    
    # Initiate highest product of 3 numbers
    high_prod3 = lst[0]*lst[1]*lst[2]
    
    # Iterate through list
    for num in lst[2:]:
        
        # Compare possible highest product of 3 numbers
        high_prod3 = max(high_prod3,num*high_prod2,num*low_prod2)
        
        
        # Check for possible new highest products of 2 numbers
        high_prod2 = max(high_prod2,num*high,num*low)
        
        # Check for possible new lowest products of 2 numbers
        low_prod2 = min(low_prod2,num*high,num*low)
        
        # Check for new possible high
        high = max(high,num)
        
        # Check for new possible low
        low = min(low,num)
        
    return high_prod3

l = [-5,-5,1,3]

print(solution(l))