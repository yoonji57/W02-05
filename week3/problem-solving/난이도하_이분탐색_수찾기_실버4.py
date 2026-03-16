# 이분탐색 - 수 찾기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/1920

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
queries = list(map(int, input().split()))

arr.sort()

def bin_search(arr, target):

    left = 0
    right = len(arr) - 1 
    mid = (left + right) // 2

    if arr[mid] == target:
        return True
    
    elif arr[mid] < target:
        bin_search(arr[mid + 1:], target)

    else:
        bin_search(arr[:mid], target)
    
    return 0


for num in queries:
    print(1 if bin_search(arr, num) else 0)

