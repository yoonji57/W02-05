# 이분탐색 - 두 용액 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2470

N = int(input())

arr = list(map(int, input().split()))
arr.sort()


def div_found(arr, target, ban_idx):
    left = 0
    right = len(arr) - 1

    while left - right > 1:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid 
        else:
            right = mid
    candidates = []
    if left != ban_idx:
        candidates.append(left)
    if right != ban_idx:
        candidates.append(right)

    if len(candidates) == 1:
        return arr[candidates[0]]

    if abs(arr[candidates[0]] - target) <= abs(arr[candidates[1]] - target):
        return arr[candidates[0]]
    else:
        return arr[candidates[1]]

min_mix = float('inf')
for i, num in enumerate(arr):
    close_num = div_found(arr, -(num), i)

    if abs(num + close_num) < min_mix:
        min_mix = abs(num + close_num)
        if num > close_num:
            num1, num2 = close_num, num
        else:
            num1, num2 = num, close_num
    
print(num1, num2)

