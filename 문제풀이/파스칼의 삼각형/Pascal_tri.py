import sys
sys.stdin = open("input.txt", "r")

def Pascal_tri(N):
    M = [[1]*N for _ in range(N)]
    for i in range(N):
        for j in range(1,i):
            M[i][j] = M[i-1][j-1] + M[i-1][j]

    for i in range(N):
        for j in range(i+1):
            if j == i:
                print(M[i][j])
            else:
                print(M[i][j], end=' ')


T = int(input())
for test_case in range(T):
    N = int(input())
    print(f'#{test_case + 1}')
    Pascal_tri(N)
