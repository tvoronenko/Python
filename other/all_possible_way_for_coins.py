#order is not important
def solution(n, coins):
    arr = [1] + [0] * n
    for coin in coins:
        for i in range(coin, n + 1):
            arr[i] += arr[i - coin]
    return arr[n]
    
print(solution(6, [1, 3, 5, 10]))    