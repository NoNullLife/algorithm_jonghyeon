import sys
sys.stdin = open("sample_input.txt", "r")

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def cnt_rflt(N, L):
    current_i = 0
    current_j = 0
    direction = 0
    cnt_rflt = 0
    while 0 <= current_i < N and 0 <= current_j < N:

        if L[current_i][current_j] == 1:
            cnt_rflt += 1

            if direction == 0:
                direction = 3
            elif direction == 3:
                direction = 0
            elif direction == 1:
                direction = 2
            elif direction == 2:
                direction = 1

        if L[current_i][current_j] == 2:
            cnt_rflt += 1

            if direction == 0:
                direction = 1
            elif direction == 1:
                direction = 0
            elif direction == 2:
                direction = 3
            elif direction == 3:
                direction = 2

        current_i += dy[direction]
        current_j += dx[direction]

    return cnt_rflt


T = int(input())
for test_case in range(T):
    N = int(input())
    L = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{test_case + 1}', cnt_rflt(N, L))
