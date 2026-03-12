# 재귀함수 - 하노이 탑 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/1914



N = int(input())

def hanoi(n, start, mid, end):

    if n == 1:
        print(start, end)
        return
    hanoi(n-1, start, end, mid)
    print(start, end)
    hanoi(n-1, mid, start, end)

print(2 ** N - 1)
if N <= 20:
    hanoi(N, 1, 2, 3)