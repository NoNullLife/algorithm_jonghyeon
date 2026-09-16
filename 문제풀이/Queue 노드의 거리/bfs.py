import sys
sys.stdin = open("sample_input.txt", "r")

from collections import deque


def L_to_graph(L, V, E):
    """간선 정보를 그래프로 가공"""

    graph = [[] for _ in range(V + 1)]
    for i in range(E):

        # 간선이 양방향이므로 양쪽으로 연결이 가능해야한다.
        graph[L[i][0]].append(L[i][1])
        graph[L[i][1]].append(L[i][0])

    return graph


def bfs(graph, V, S, G):

    # 체크리스트 및 큐우 생성, 시작점 append
    visited = [0] * (V + 1)  # 그런데 왜 V+1인 것????? 인덱싱 바로 하려고????  <- 네.
    que = deque()
    que.append(S)

    # que로 while 걸기
    while que:
        """
            새로 방문하는 경우를 제외하고,
            que는 계속 줄어든다.
            que가 비지 않는 한, 반복을 계속 하기로 한다.....?
            ---------------------------------------------------
            차라리 도달하면 바로 탐색 종료하고,
            끝끝내 도달 못했을 때, 0을 반환하는게 낫지 않나?
        """

        # deque 수행
        current_node = que.popleft()

        # 혹시라도 목적지면 탐색 종료
        if current_node == G:
            return visited[current_node]

        # 탐색 수행
        for next_node in graph[current_node]:

            # 방문 안한 노드는 que에 추가를 해주어야한다.
            if not visited[next_node]:
                que.append(next_node)

                """
                visited는 단순한 체크리스트가 아니다.
                현재까지 몇 스탭을 밟았는지를 기록하는 지표로 삼아야한다.
                (시작점은 스탭에 포함하지 않으므로 0이다.)
                """
                visited[next_node] = visited[current_node] + 1

    return 0


T = int(input())
for test_case in range(T):
    V, E = list(map(int, input().split()))
    L = [list(map(int, input().split())) for _ in range(E)]
    S, G = list(map(int, input().split()))
    graph = L_to_graph(L, V, E)
    print(f'#{test_case + 1}', bfs(graph, V, S, G))
