# 분할정복 - 색종이 만들기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/2630

N = int(input())

square = [list(map(int, input().split())) for _ in range(N)]

def divide_conquer(square, x_left, x_right, y_left, y_right):

    same, first = same_color(square, x_left, x_right, y_left, y_right)
    count_white, count_blue = 0, 0
    # base case
    if same:
        if first == 0:
            count_white += 1
        else:
            count_blue += 1
    
    x_mid = (x_left + x_right) // 2
    y_mid = (y_left + y_right) // 2

    divide_conquer(square, x_left, x_mid, y_left, y_mid)
    divide_conquer(square, x_mid + 1, x_right, y_left, y_mid)
    divide_conquer(square, x_left, x_mid, y_mid + 1, y_right)
    divide_conquer(square, x_mid + 1, x_right, y_mid + 1, y_right)

    print(count_white)
    print(count_blue)

    

def same_color(square, x_left, x_right, y_left, y_right):
    first = square[x_left][y_left]
    for y in range(y_left, y_right + 1):
        for x in range(x_left, x_right + 1):
            if square[y][x] != first:
                return False, first
    return True, first