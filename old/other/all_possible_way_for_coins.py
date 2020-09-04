import unittest

#order is not important
def solution(n, coins):
    arr = [1] + [0] * n
    for coin in coins:
        for i in range(coin, n + 1):
            arr[i] += arr[i - coin]
    return arr[n]

#order is important
def solution1(n, coins):
    if n is None or n < 0 or coins is None or len(coins)==0:
        raise ValueError("Incorrect value: check sum n or array of coins")
    arr = [0 for x in range(n+1)]
    arr[0] = 1
    for i in range(0,n+1):
        for coin in coins:
            if (i - coin)>=0:
                arr[i] += arr[i-coin]
    return arr[n]

def main():
    """test"""
    print(solution1(10, [2,5,3,6]))
    print(solution(10, [2,5,3,6]))

if __name__ == '__main__':
    main()