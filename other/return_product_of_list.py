def product(arr):
    product = 1
    len_arr= len(arr)
    output = []
    output.append(product)
    for i in range(1,len_arr):
        output.append(product)
        product = product * arr[i] 
    product = output[0]
    for i in range(len_arr-1,-1,-1):
        output[i] = product*output[i]
        product = product * arr[i]
    return output

print(product([1,2,3,4]))