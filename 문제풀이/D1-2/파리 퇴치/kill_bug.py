import sys
sys.stdin = open("input.txt", "r")


def kill(N, M, B):
    max_kill = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            kill = sum([B[i + mi][j + mj] for mi in range(M) for mj in range(M)])
            if kill > max_kill:
                max_kill = kill

    return max_kill


T = int(input())
for test_case in range(T):
    N, M = list(map(int, input().split()))
    B = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{test_case + 1}', kill(N, M, B))
