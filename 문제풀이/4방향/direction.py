import sys
sys.stdin = open("sample_input.txt", "r")


def distance_sum(M, N):
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    result = 0
    for i in range(N):
        for j in range(N):
            for k in range(4):
                tempi = i + di[k]
                tempj = j + dj[k]
                if 0 <= tempi < N and 0 <= tempj < N:
                    result += abs(M[i][j] - M[tempi][tempj])

    return result

T = int(input())
for test_case in range(T):
    N = int(input())
    M = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{test_case + 1}', distance_sum(M, N))
