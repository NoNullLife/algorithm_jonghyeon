import sys
sys.stdin = open("sample_input.txt", "r")


def find_pattern(str1, str2):
    N = len(str1)
    M = len(str2)
    for i in range(M-N+1):
        trigger = True
        for j in range(N):
            if str1[j] != str2[i+j]:
                trigger = False
                break
        if trigger:
            return i

    return -1


T = int(input())
for test_case in range(T):
    str1 = list(input())
    str2 = list(input())
    print(f'#{test_case + 1}', find_pattern(str1, str2))
