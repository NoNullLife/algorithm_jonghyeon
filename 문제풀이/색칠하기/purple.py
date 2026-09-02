import sys
sys.stdin = open("sample_input.txt", "r")


def purple(M):
    red_M = [row for row in M if row[-1] == 1]
    blue_M = [row for row in M if row[-1] == 2]
    red_field = {(i, j) for row in red_M for i in range(row[0], row[2] + 1) for j in range(row[1], row[3] + 1)}
    blue_field = {(i, j) for row in blue_M for i in range(row[0], row[2] + 1) for j in range(row[1], row[3] + 1)}

    purple_field = red_field & blue_field
    return len(purple_field)


T = int(input())
for test_case in range(T):
    N = int(input())
    M = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{test_case + 1}', purple(M))
