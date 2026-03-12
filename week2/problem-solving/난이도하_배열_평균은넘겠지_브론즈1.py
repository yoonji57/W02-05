# 배열 - 평균은 넘겠지 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/4344

C = int(input())

for _ in range(C):
    count = 0
    data = list(map(int, input().split()))
    n = data[0]
    scores = data[1:]
    avg = sum(scores) / n 
    for i in range(n):
        if scores[i] > avg: 
            count += 1 
    print(f"{count/n*100:.3f}%") 