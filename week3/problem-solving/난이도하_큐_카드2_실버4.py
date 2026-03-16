# 큐 - 카드2 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/2164

from collections import deque

N = int(input())

arr = deque(range(1, N+1))


while arr:
    if len(arr) == 1:
        print(arr.pop())
        break 
    arr.popleft()
    arr.append(arr.popleft())

