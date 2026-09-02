import sys
sys.stdin = open("sample_input.txt", "r")


def fall(L, N):
    M = []
    for i in L:
        M.append([1] * i + [0] * (100 - i))
    r = 0
    for i in range(100):
        z = 0
        trigger = False
        for j in range(N):
            if M[j][i] == 1:
                trigger = True
            if M[j][i] == 0 and trigger == True:
                z += 1
        if trigger == False:
            break

        if z > r:
            r = z

    return r


T = int(input())
for test_case in range(T):
    N = list(map(int, input().split()))[0]
    L = list(map(int, input().split()))
    print(f'#{test_case + 1}', fall(L, N))
