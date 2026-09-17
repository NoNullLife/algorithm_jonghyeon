import sys
sys.stdin = open("sample_input.txt", "r")

Map = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
cnt = [0] * 10


def G_sort(L):
    idx = map(lambda x: Map.index(x), L)
    idx = sorted(idx)
    return ' '.join(list(map(lambda x: Map[x], idx)))


T = int(input())
for test_case in range(T):
    N = int(input())
    L = input().split()
    print(f'#{test_case + 1}', G_sort(L))
