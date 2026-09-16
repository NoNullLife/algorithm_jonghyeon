import sys
sys.stdin = open("sample_input.txt", "r")

from collections import deque


def last_pizza(N, M, C):
    # (피자 번호 1-based, 치즈 양) 형태로 화덕 큐를 초기화합니다.
    # 처음에는 화덕 크기 N만큼 피자를 순서대로 넣습니다.
    hwaduck = deque([[i + 1, C[i]] for i in range(N)])

    # 다음에 화덕에 들어갈 피자의 인덱스 (N번 피자부터 대기)
    next_idx = N

    # 화덕에 피자가 1개 남을 때까지 반복합니다.
    while len(hwaduck) > 1:
        # 1. 화덕의 입구(맨 앞)에서 피자를 꺼냅니다.
        pizza_num, cheese = hwaduck.popleft()

        # 2. 치즈를 반으로 줄입니다.
        cheese //= 2

        # 3-1. 치즈가 남아있다면 다시 화덕 맨 뒤로 넣습니다.
        if cheese > 0:
            hwaduck.append([pizza_num, cheese])

        # 3-2. 치즈가 다 녹았고, 아직 안 넣은 피자가 있다면 새 피자를 화덕에 넣습니다.
        elif next_idx < M:
            hwaduck.append([next_idx + 1, C[next_idx]])
            next_idx += 1

    # 마지막으로 남은 피자의 번호를 반환합니다.
    return hwaduck[0][0]


T = int(input())
for test_case in range(T):
    N, M = list(map(int, input().split()))
    C = list(map(int, input().split()))
    print(f"#{test_case + 1}", last_pizza(N, M, C))
