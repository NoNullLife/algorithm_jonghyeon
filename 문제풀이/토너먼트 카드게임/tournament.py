import sys
sys.stdin = open("sample_input.txt", "r")


def find_winner(N,L):
    pass


T = int(input())
for test_case in range(T):
    N = int(input())
    L = list(map(int, input().split()))
    print(f'#{test_case + 1}', find_winner(N,L))
