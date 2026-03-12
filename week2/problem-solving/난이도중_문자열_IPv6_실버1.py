# 문자열 - IPv6 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/3107



IPv6 = input()

if "::" in IPv6:
    left, right = IPv6.split("::")

    left_parts = left.split(":") if left else []
    right_parts = right.split(":") if right else []

    missing = 8 - (len(left_parts) + len(right_parts))
    IPv6 = left_parts + (["0000"] * missing) + right_parts



else:
    IPv6 = IPv6.split(':')
    
for i in range(8):
        while len(IPv6[i]) < 4:
            IPv6[i] = '0' + IPv6[i]
print(':'.join(IPv6))    