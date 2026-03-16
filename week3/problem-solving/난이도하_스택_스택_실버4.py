# 스택 - 스택 (백준 실버 4)
# 문제 링크: https://www.acmicpc.net/problem/10828

import sys
input = sys.stdin.readline

N = int(input())
stack = []

for _ in range(N):
    cmd = input().split()
    # result = []
    # for 문 안에 넣어두면 매번 스택이 새 리스트로 초기화됨
    if cmd[0] == "push":
        stack.append(stack[1])
    
    elif cmd[0] == "pop":
        if len(stack)== 0:
            print("-1")
        else:
            print(stack.pop())

    elif cmd[0] == "size":
        print(len(stack))

    elif cmd[0] == "empty":
        if not stack:
            print("1")
        else:
            print("0")
            
    elif cmd[0] == "top":
        if not stack:
            print("-1")
        else:
            print(stack[-1])