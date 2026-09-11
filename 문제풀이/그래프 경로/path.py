import sys
sys.stdin = open("sample_input.txt", "r")


def DFS_with_stack(V, L, start, end):
    graph = [[] for _ in range(V)]
    for i in L:
        graph[i[0]].append(i[1])

    visited = [False]*(V+1)
    visited[start] = True
    stack = []
    current_node = start

    while True:
        trigger = True
        for next_node in graph[current_node]:
            if not visited[next_node]:
                trigger = False
                stack.append(current_node)
                current_node = next_node
                visited[current_node] = True

        if trigger:

            if stack == []:
                break
            else:
                current_node = stack.pop()

        if current_node == end:
            return 1

    return 0




T = int(input())
for test_case in range(T):
    V, E = map(int, input().split())
    L = [list(map(int, input().split())) for _ in range(E)]
    start, end = map(int, input().split())
    print(f'#{test_case + 1}', DFS_with_stack(V, L, start, end))
