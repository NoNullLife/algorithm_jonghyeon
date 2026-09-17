import sys
sys.stdin = open("sample_input.txt", "r")

from collections import deque


def rotation(M, L):
    q = deque(L)
    for _ in range(M):
        q.append(q.popleft())

    return q.popleft()


T = int(input())
for test_case in range(T):
    N, M = list(map(int, input().split()))
    L = list(map(int, input().split()))
    print(f'#{test_case + 1}', rotation(M, L))
