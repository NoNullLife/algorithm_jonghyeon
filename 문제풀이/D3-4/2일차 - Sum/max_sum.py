import sys
sys.stdin = open("input.txt", "r")


def max_sum(M):
    sum = []

    cross_1 = 0
    cross_2 = 0

    for i in range(100):
        cross_1 += M[i][i]
        cross_2 += M[99 - i][i]

        row_sum = 0
        col_sum = 0
        for j in range(100):
            row_sum += M[i][j]
            col_sum += M[j][i]

        sum.append(row_sum)
        sum.append(col_sum)
    sum.append(cross_1)
    sum.append(cross_2)

    return max(sum)


T = 10
for test_case in range(T):
    N = input()
    M = [list(map(int, input().split())) for _ in range(100)]
    print(f'#{test_case + 1}', max_sum(M))
