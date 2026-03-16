# 분할정복 - 곱셈 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1629

A, B, C = list(map(int, input().split()))


# 첫째 줄에 A를 B번 곱한 수를 C로 나눈 나머지를 출력한다.
# (a * b) % c = ((a % c) * (b % c)) % c

def mul(A, B):
    if B == 1:
        return A % C

    temp = mul(A, B // 2)

    if B % 2 == 1:
        return (temp * temp * A) % C

    else:
        return (temp * temp) % C


print(mul(A, B) % C)
