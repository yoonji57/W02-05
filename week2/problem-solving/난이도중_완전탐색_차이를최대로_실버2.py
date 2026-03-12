# 완전탐색 - 차이를 최대로 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10819


N = int(input())

nums = list(map(int, input().split()))

answer = 0

def arr(now, cost, count):
    global answer

    if count == N:
        answer = max(cost, answer)
        return 

    for next in range(N):
        if not visited[next]:
            visited[next] = True
            arr(next, cost + abs(nums[next] - nums[now]), count + 1)
            visited[next] = False


for start in range(N):
    visited = [False] * N 
    visited[start] = True    
    arr(start, 0, 1)

print(answer)
