import sys

sys.stdin = open("sample_input.txt", "r")


def get_min_cost(matrix, n, visited=None, row=0, current_sum=0, min_so_far=90):
    # 최초 호출 시 visited 초기화
    if visited is None:
        visited = [False] * n

    # [가지치기] 이미 현재까지의 합이 알고 있는 최솟값 이상이면 더 이상 탐색하지 않고 반환
    if current_sum >= min_so_far:
        return min_so_far

    # [종료 조건] 모든 행(row)에 대해 열 선택을 마쳤을 때 현재 합 반환
    if row == n:
        return current_sum

    # 재귀 호출 및 최솟값 갱신
    for col in range(n):
        if not visited[col]:
            visited[col] = True

            # 다음 행으로 넘어갈 때 current_sum과 현재까지의 min_so_far를 전달하고 결과를 받음
            cost = get_min_cost(matrix, n, visited, row + 1, current_sum + matrix[row][col], min_so_far)

            # 하위 재귀 탐색에서 찾은 최솟값으로 min_so_far 갱신
            min_so_far = min(min_so_far, cost)

            visited[col] = False  # 백트래킹

    return min_so_far


T = int(input())
for test_case in range(T):
    N = int(input())
    L = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{test_case + 1}', get_min_cost(L, N))
