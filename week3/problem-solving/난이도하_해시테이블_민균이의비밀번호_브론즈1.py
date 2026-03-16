# 해시 테이블 - 민균이의 비밀번호 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/9933

N = int(input())
chars = [input() for i in range(N)]

for char in chars:
    reserve_char = char[::-1]
    if reserve_char in chars:
        print(len(char), char[len(char)//2])
        break

# break 넣는 걸 빼먹음 