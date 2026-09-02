import sys
sys.stdin = open("input1.txt", "r")


def compute_max_score(B, N, M):
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    max_score = 0
    for i in range(N):
        for j in range(M):
            score = B[i][j]
            for k in range(4):
                tempi = i + di[k]
                tempj = j + dj[k]
                if 0 <= tempi < N and 0 <= tempj < M:
                    score += B[tempi][tempj]

            if score > max_score:
                max_score = score

    return max_score


T = int(input())
for test_case in range(T):
    N, M = list(map(int, input().split()))
    B = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{test_case + 1}', compute_max_score(B, N, M))
