import sys
sys.stdin = open("sample_input.txt", "r")


# 끝점에서 가로, 세로, 대각선1, 대각선2로 4개 방향만 고려하여 검사하면 된다.
dr = [0, 1, 1, -1]
dc = [1, 0, 1, 1]
direction_list = [0, 1, 2, 3]


def check_5(N, L, start_r, start_c, direction):
    # 좌표가 범위를 벗어나는 경우에 대한 예외처리
    end_r, end_c = start_r + dr[direction] * 4, start_c + dc[direction] * 4
    if not (0 <= end_r < N and 0 <= end_c < N):
        return False

    else:
        # 정해진 방향으로 5칸을 확인하며 돌이 끊기지 않는지 확인
        for i in range(5):
            if L[start_r + dr[direction] * i][start_c + dc[direction] * i] == '.':
                return False

        return True


def determination(N, L):
    for start_r in range(N):
        for start_c in range(N):
            for direction in direction_list:
                if check_5(N, L, start_r, start_c, direction):
                    return 'YES'

    return 'NO'


T = int(input())
for test_case in range(T):
    N = int(input())
    L = [list(input()) for _ in range(N)]
    print(f'#{test_case + 1}', determination(N, L))
