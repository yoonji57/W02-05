# 파이썬 문법 - 최댓값 (백준 브론즈3)
# 문제 링크: https://www.acmicpc.net/problem/2562


nums = [int(input()) for _ in range(9)]

max_num = 0
count = 0

for i, num in enumerate(nums, start=1):
    if num > max_num:
        max_num = num
        count = i

print(max_num)
print(count)