import sys
sys.stdin = open("sample_input.txt", "r")

L = list(range(1, 13))


def power_set_N(N, K):
    power_set_N = 0
    for i in range(2 ** 12):
        subset = []
        cnt = 0
        sum_of_subset = 0
        for j in range(12):
            if i & (1 << j):
                subset.append(L[j])
                sum_of_subset += L[j]
                cnt += 1
        if cnt == N and sum_of_subset == K:
            power_set_N += 1

    return power_set_N


T = int(input())
for test_case in range(T):
    N, K = list(map(int, input().split()))
    print(f'#{test_case + 1}', power_set_N(N, K))
