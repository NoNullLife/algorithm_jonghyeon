import sys
sys.stdin = open("sample_input.txt", "r")



T = int(input())
for test_case in range(T):
    N, M = list(map(int, input().split()))
    L = list(map(int, input().split()))
    print(f'#{test_case + 1}', L)
