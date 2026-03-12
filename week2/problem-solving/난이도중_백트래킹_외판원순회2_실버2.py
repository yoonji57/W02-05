# 백트래킹 - 외판원 순회 2 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10971

N = int(input()) 

W = [list(map(int, input().split())) for _ in range(N)]

answer = float('inf')

def BacktrackTSP(now, cost, count):
    global answer

    if cost >= answer:
        return 

    if count == N:
        # 다시 시작점으로 갈 수 있으면 정답 갱신
        if W[now][start] != 0:
            answer = min(answer, cost + W[now][start])  
        return 

    for next in range(N):
        if not visited[next] and W[now][next] != 0:
            visited[next] = True
            BacktrackTSP(next, cost + W[now][next], count + 1)
            visited[next] = False


for start in range(N):
    visited = [False] * N 
    visited[start] = True    
    BacktrackTSP(start, 0, 1)

print(answer)