import sys
sys.stdin = open("sample_input.txt", "r")

# 상, 하, 좌, 우 이동을 위한 방향 벡터
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(r, c, N, L, visited):
    # 1. 목적지(값 3)에 도착한 경우 성공(1) 반환
    if L[r][c] == 3:
        return 1

    # 2. 방문 체크
    visited[r][c] = True

    # 3. 인접 정점(상/하/좌/우 4방향) 탐색
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]

        # 미로 범위 내에 있고, 벽(1)이 아니며, 방문하지 않은 경우
        if 0 <= nr < N and 0 <= nc < N:
            if L[nr][nc] != 1 and not visited[nr][nc]:
                # 하위 경로 탐색 중 목적지에 도착했으면 즉시 1 반환
                if dfs(nr, nc, N, L, visited):
                    return 1

    # 모든 경로를 탐색했지만 목적지에 도달하지 못한 경우 실패(0) 반환
    return 0


def maze(N, L):
    visited = [[False] * N for _ in range(N)]

    # 시작점(2) 찾기
    for r in range(N):
        for c in range(N):
            if L[r][c] == 2:
                start_r, start_c = r, c
                break

    # DFS 실행 후 결과 반환 (도착 가능: 1, 불가능: 0)
    return dfs(start_r, start_c, N, L, visited)


T = int(input())
for test_case in range(T):
    N = int(input())
    L = [list(map(int, input())) for _ in range(N)]
    print(f'#{test_case + 1}', maze(N, L))
