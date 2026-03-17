# 링크드리스트 - 에디터 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1406

import sys
input = sys.stdin.readline

chars = input().rstrip()
M = int(input())


class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None 
        self.next = None

ans = Node(None)
cursor = ans

for ch in chars:
    node = Node(ch)

    cursor.next = node
    node.prev = cursor

    cursor = node 

for _ in range(M):

    cmd = input().split()
    

    if cmd[0] == 'L':
        if cursor.prev is not None:
            cursor = cursor.prev
    
    elif cmd[0] == 'D':
        if cursor.next is not None:
            cursor = cursor.next

    elif cmd[0] == 'B':
        if cursor.prev is not None:
            prev_node = cursor.prev
            next_node = cursor.next
            prev_node.next = next_node
            if next_node:
                next_node.prev = prev_node

            cursor = prev_node
    
    else:
        new_node = Node(cmd[1])
        next_node = cursor.next

        cursor.next = new_node
        new_node.prev = cursor

        new_node.next = next_node
        if next_node:

            next_node.prev = new_node
        cursor = new_node


cur = ans.next
result = []

while cur:
    result.append(cur.val)
    cur = cur.next 

print(''.join(result))

