import sys
sys.stdin = open("sample_input.txt", "r")




T = int(input())
for test_case in range(T):
    E, N = map(int, input().split())
    L = list(map(int, input().split()))
    graph = {}
    for i in range(E):
        graph.setdefault(L[2 * i], []).append(L[2 * i + 1])
    print(f'#{test_case + 1}', graph)
