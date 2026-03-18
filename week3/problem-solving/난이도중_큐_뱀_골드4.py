# 큐 - 뱀 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/3190

N = int(input())
K = int(input())

board = [[0] * N for _ in range(N)]  # N x N, 0으로 채움. 사과 있는 칸만 1로 표시 


apple = []
for _ in range(K):
    row, col = map(int, input().split())
    apple.append((row, col))

L = int(input())
snake = [] # queue
time_count = 0

for _ in range(L):
    X, C = input().split()
    X = int(X)

    if C == 'L':
        
    elif C == 'D':

    