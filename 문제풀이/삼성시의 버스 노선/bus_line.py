import sys

sys.stdin = open("s_input.txt", "r")























T = int(input())
for test_case in range(T):
    N = int(input())

    AB = []
    for i in range(N):
        AB.append(list(map(int, input().split())))

    P = int(input())
    C = [0] * P
    for j in range(P):
        C[j] = int(input())

    print(f'#{test_case + 1}')
