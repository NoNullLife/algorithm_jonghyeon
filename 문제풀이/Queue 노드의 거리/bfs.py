import sys
sys.stdin = open("sample_input.txt", "r")

from collections import deque


def L_to_graph(L, V, E):
    """간선 정보를 그래프로 가공"""

    graph = [[] for _ in range(V + 1)]
    for i in range(E):
        graph[L[i][0]].append(L[i][1])
        graph[L[i][1]].append(L[i][0])

    return graph


def f(graph, V, S, G):
    visited = [0] * (V + 1)  # 왜 V+1인 것????? 인덱싱 바로 하려고????  <- 네.
    que = deque()
    que.append(S)

    while que:
        t = que.popleft()

        for next_node in graph[t]:
            if not visited[next_node]:
                que.append(next_node)
                visited[next_node] = visited[t] + 1

    return visited[G]


T = int(input())
for test_case in range(T):
    V, E = list(map(int, input().split()))
    L = [list(map(int, input().split())) for _ in range(E)]
    S, G = list(map(int, input().split()))
    graph = L_to_graph(L, V, E)
    print(f'#{test_case + 1}', f(graph, V, S, G))
