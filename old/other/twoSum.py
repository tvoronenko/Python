def find_sum(arr,posible_sum):
    found = False
    seen = set()
    for i in arr:
        target = posible_sum  - i
        if target in seen:
            return True
        seen.add(i)
    return found

def find_pair_witout_ducplicate(arr,posible_sum):
    output = set()
    seen = set()
    for i in arr:
        target = posible_sum  - i
        if target in seen:
            output.add((min(i,target), max(i,target)))
        seen.add(i)
    return output

def find_pair_with_ducplicate(arr,posible_sum):
    output = {}
    seen = set()
    for i in arr:
        target = posible_sum  - i
        if target in seen:
            output[i] = target
        seen.add(i)
    return output
            
    
print(find_pair_with_ducplicate([1,2,4,3,2,1],5))
print(find_pair_with_ducplicate([1,3,5,1,7],14))