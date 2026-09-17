import sys
sys.stdin = open("sample_input.txt", "r")


T = int(input())
for test_case in range(T):
    A, B = input().split()
    cnt = 0
    for i in A.split(B):
        cnt += len(i)
    print(f'#{test_case + 1}', len(A.split(B))+cnt-1)
