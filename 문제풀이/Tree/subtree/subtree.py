import sys
sys.stdin = open("sample_input.txt", "r")


def cnt_node(graph, current_node):
    cnt = 1
    for next_node in graph[current_node]:
        cnt += cnt_node(graph, next_node)

    return cnt


T = int(input())
for test_case in range(T):
    E, N = map(int, input().split())
    L = list(map(int, input().split()))
    graph = [[] for _ in range(E + 2)]
    for i in range(E):
        graph[L[2 * i]].append(L[2 * i + 1])
    print(f'#{test_case + 1}', cnt_node(graph, N))
