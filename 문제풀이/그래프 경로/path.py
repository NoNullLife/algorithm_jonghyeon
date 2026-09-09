import sys
sys.stdin = open("sample_input.txt", "r")



T = int(input())
for test_case in range(T):
    V, E = map(int, input().split())
    L = [list(map(int, input().split())) for _ in range(E)]
    start, end = map(int, input().split())
    print(f'#{test_case + 1}')
    print(V, E)
    print(L)
    print(start, end)
