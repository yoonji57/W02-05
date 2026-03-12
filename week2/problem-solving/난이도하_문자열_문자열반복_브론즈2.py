# 문자열 - 문자열 반복 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/2675

 
T = int(input())

for i in range(T):
    R, S = input().split()
    for char in S:
        print(char* int(R), end='')
    print()