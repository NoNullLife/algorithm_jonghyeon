import sys
sys.stdin = open("sample_input.txt", "r")




T = int(input())
for test_case in range(T):
    N = int(input())
    L = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{test_case + 1}', L)
