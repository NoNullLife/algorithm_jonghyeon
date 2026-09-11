import sys
sys.stdin = open("sample_input.txt", "r")


def dfs(current_node):
    # 1. 목적지에 도착한 경우 성공(1) 반환
    if current_node == end:
        return 1

    # 2. 방문 체크
    visited[current_node] = True

    # 3. 인접 정점 탐색
    for next_node in graph[current_node]:
        if not visited[next_node]:

            # 하위 경로 탐색 중 목적지에 도착했으면(1을 리턴받았으면) 즉시 1 반환
            if dfs(next_node):
                return 1

    # 모든 경로를 탐색했지만 목적지에 도달하지 못한 경우 실패(0) 반환
    return 0


T = int(input())
for test_case in range(T):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)
    for _ in range(E):
        s, e = map(int, input().split())
        graph[s].append(e)
    start, end = map(int, input().split())
    print(f'#{test_case + 1}', dfs(start))
