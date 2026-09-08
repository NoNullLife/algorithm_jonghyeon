import sys
sys.stdin = open("3_sample_input.txt", "r")










T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    d = [0] * N
    p = [0] * N
    I = [0] * N
    g = [0] * M
    L = [0] * M

    for i in range(N):
        d[i], p[i], I[i] = map(int, input().split())

    for j in range(M):
        g[j], L[j] = map(int, input().split())

    print(f'#{test_case + 1}', N,M,d,p,I,g,L)
