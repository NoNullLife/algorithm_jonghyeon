import sys
sys.stdin = open("sample_input.txt", "r")


def good(L):
    r = 0
    for i in range(2, len(L) - 2):
        g = L[i]
        m = max([L[i - 2], L[i - 1], L[i + 1], L[i + 2]])
        g -= m
        if g > 0:
            r += g

    return r


for test_case in range(10):
    N = int(input())
    L = list(map(int, input().split()))

    print(f'#{test_case + 1}', good(L))