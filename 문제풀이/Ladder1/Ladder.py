import sys
sys.stdin = open("input.txt", "r")


dr = [-1, 0, 0]
dc = [0, -1, 1]


# 재귀로 안풀거임.
def try_Ladder(M):

    # 먼저 끝 줄에서 2를 찾아봅시다
    for idx, item in enumerate(M[-1]):
        if item == 2:
            current_r = 99
            current_c = idx
            break

    # 찾았니? 그럼 이제 방향 탐색 하셔야죠?

    direction = 0  # 처음엔 위쪽 방향을 바라봅니다.
    while current_r > 0:
        # 위쪽 바라보면서 가다가 만약 옆에 0 아니고 1이면 어떻게 해야해요? 방향 틀어야해요.
        # 맨 왼쪽이면 왼쪽을 검사할 필요가 없고, 맨 오른쪽이면 오른쪽을 검사할 필요가 없어요.

        if current_c > 0 and M[current_r][current_c - 1] == 1 and direction == 0:
            direction = 1

        elif current_c < 99 and M[current_r][current_c + 1] == 1 and direction == 0:
            direction = 2

        # 다음 좌표를 계산해줍시다.
        next_r, next_c = current_r + dr[direction], current_c + dc[direction]

        # 범위를 벗어났거나 막혀있으면 다시 위로 향합니다.
        if next_c < 0 or next_c > 99 or M[next_r][next_c] == 0:
            direction = 0
            current_r -= 1

        # 아니라면 그대로 좌표를 업데이트합니다.
        else:
            current_r, current_c = next_r, next_c

    return current_c


for _ in range(10):
    T = int(input())
    M = [list(map(int, input().split())) for _ in range(100)]
    print(f'#{T}', try_Ladder(M))
