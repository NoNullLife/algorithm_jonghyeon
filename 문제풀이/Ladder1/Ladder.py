import sys
sys.stdin = open("input.txt", "r")


def try_Ladder(M):
    for j in range(102):
        current_i = 0
        current_j = j
        if M[0][current_j] == 0:
            continue

        while current_i < 99:
            current_i += 1
            trigger = True

            if M[current_i][current_j - 1] == 1 and trigger:
                current_j = left(current_j, M[current_i])
                trigger = False

            if M[current_i][current_j + 1] == 1 and trigger:
                current_j = right(current_j, M[current_i])
                trigger = False



        if M[current_i][current_j] == 2:
            return current_j


def left(current_j, row):
    for j in range(current_j, 0, -1):
        if row[j - 1] == 0:
            return j




def right(current_j, row):
    for j in range(current_j, 101):
        if row[j + 1] == 0:
            return j


T = int(input())
for test_case in range(T):
    M = [[0]+list(map(int, input().split()))+[0] for _ in range(100)]
    print(f'#{test_case + 1}', try_Ladder(M))
