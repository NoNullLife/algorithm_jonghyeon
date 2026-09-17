import sys

sys.stdin = open("sample_input.txt", "r")


def move(current_idx, K, N, M):
    move_limit = current_idx + K
    if move_limit >= N:  # k만큼 이동해서 종점 넘어가면 최댓값인 N을 반환
        return N

    most_far_supply_station = -1  # 가장 멀리 있는 충전소를 탐색
    for idx in range(move_limit, current_idx, -1):
        if idx in supply_station_idx:
            most_far_supply_station = idx
            break
    if most_far_supply_station == -1:  # 충전소가 중간에 없으면 더이상 진행 불가하므로 False를 반환
        return False

    return most_far_supply_station


def compute_supply_num(K, N, M):
    current_idx = 0
    supply_num = 0
    while True:
        most_far_supply_station = move(current_idx, K, N, M)  # 얘가 숫자인지 False인지 아직 모름

        if not most_far_supply_station:  # 이동할 수 없으면 0 반환
            return 0

        # 숫자면 그 인덱스로 이동한다는 것. 현재위치를 해당 인덱스로 업데이트한다.
        current_idx = most_far_supply_station

        if current_idx == N:
            return supply_num
        else:
            supply_num += 1


T = int(input())
for test_case in range(T):
    K, N, M = list(map(int, input().split()))
    supply_station_idx = list(map(int, input().split()))

    print(f'#{test_case + 1}', compute_supply_num(K, N, M))
