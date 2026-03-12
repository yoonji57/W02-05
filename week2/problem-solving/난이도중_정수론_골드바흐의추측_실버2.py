# 정수론 - 골드바흐의 추측 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/9020

import math
T = int(input())


# 먼저 소수? 
def prime(n):
    if n < 2:
        return False

    elif n == 2:
        return True

    elif n % 2 == 0:
        return False
    
    else:
        for k in range(3, int(math.sqrt(n)) + 1, 2):
            if n % k == 0:
                return False
        return True



for i in range(T):
    n = int(input())
    for j in range(n//2, 1, -1):
        if (prime(j) == True) and (prime(n - j) == True):
            print(j, n - j)
            break


 