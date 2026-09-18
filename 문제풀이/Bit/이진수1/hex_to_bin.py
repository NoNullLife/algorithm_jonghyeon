import sys
sys.stdin = open("sample_input.txt", "r")

H_D = {
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15,
}


def Bin(N, H):
    D = 0

    i = 0
    for chr in H[::-1]:
        if chr.isdecimal():
            D += int(chr) * 16 ** i
        else:
            D += H_D[chr] * 16 ** i
        i += 1

    B = bin(D)[2:]
    r = (-len(B)) % 4
    return r*'0' + B


T = int(input())
for test_case in range(T):
    N, H = input().split()
    print(f'#{test_case + 1}', Bin(N, H))
