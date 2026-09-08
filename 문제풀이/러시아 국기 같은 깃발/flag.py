import sys
sys.stdin = open("sample_input.txt", "r")


def red_winter(N, M, F):
    require_X = []
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            not_X_cnt = 0
            not_X_cnt += ''.join(F[:i + 1]).count('W')
            not_X_cnt += ''.join(F[i + 1:j + 1]).count('B')
            not_X_cnt += ''.join(F[j + 1:]).count('R')
            require_X.append(N * M - not_X_cnt)

    return min(require_X)


T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    F = [input() for _ in range(N)]
    print(f'#{test_case + 1}', red_winter(N, M, F))
