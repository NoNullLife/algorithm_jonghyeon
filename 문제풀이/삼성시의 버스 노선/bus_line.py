import sys
sys.stdin = open("s_input.txt", "r")


def compute(P, N, AB, C):
    result = [0] * P
    for i in range(N):
        temp = [idx for idx, c in enumerate(C) if AB[i][0] <= c <= AB[i][1]]
        for idx in temp:
            result[idx] += 1

    return result


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

    print(f'#{test_case + 1}', ' '.join(map(str, compute(P, N, AB, C))))
