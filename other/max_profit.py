def max_profit(prices):
    if len(prices)<3:
        raise ValueError("Need at least two stock")
    min_i = prices[0]
    max_i = 0
    index_start = 0
    index_end=-1
    for i in range(1,len(prices)):
        tmp = index_start
        if min_i>prices[i]:
            min_i = prices[i]
            index_start = i
        if max_i<(prices[i]-min_i):
            max_i=prices[i]-min_i
            index_end = i
        else:
            index_start = tmp
    return (max_i,index_start,index_end)

prices=[12,15,16,17,2]
print(max_profit(prices))