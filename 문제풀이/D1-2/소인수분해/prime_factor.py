import sys
sys.stdin = open("input.txt", "r")


def f(N):
    exp = [0, 0, 0, 0, 0]
    temp = N
    for idx, n in enumerate([2, 3, 5, 7, 11]):
        while True:
            if temp == 1:
                break
            if temp % n != 0:
                break

            temp //= n
            exp[idx] += 1

    return ' '.join(map(str, exp))


T = int(input())
for test_case in range(T):
    N = int(input())
    print(f'#{test_case + 1}', f(N))
