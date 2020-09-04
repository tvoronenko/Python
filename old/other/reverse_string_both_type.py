def reverse(str):
    if len(str)==1:
        return str
    return reverse(str[1:])+str[0]

def reverse_inter(str):
    n = len(str)
    list_str=[]
    for c in str:
        list_str.append(c)
    for i in range(n/2):
        list_str[i],list_str[n-i-1] = list_str[n-i-1],list_str[i]
    return ''.join(list_str) 
        
print(reverse_inter("AQWER"))