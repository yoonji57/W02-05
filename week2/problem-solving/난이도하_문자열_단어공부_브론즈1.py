# 문자열 - 단어 공부 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/1157

s = input().upper()
count_aph = [0] * 26

for ch in s:
    index = ord(ch) - ord('A')
    count_aph[index] += 1

m = max(count_aph)

if count_aph.count(m) > 1: # 최댓값 m이 리스트에 몇 번 등장하는지 확인
    print("?")

else:
    # 가장 큰 값 가지는 인덱스 어떻게 구해?
    idx = count_aph.index(m)
    # index(m) -> 처음으로 m이 나온 위치
    print(chr(idx + ord('A')))

    