import sys
sys.stdin = open("sample_input.txt", "r")



T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    L = [list(input()) for _ in range(N)]
    print(f'#{test_case + 1}', L)
