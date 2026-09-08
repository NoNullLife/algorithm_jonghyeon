import sys
sys.stdin = open("sample_input.txt", "r")


def len_remainder(string):
    stack = []
    for chr in string:
        if stack == [] or stack[-1] != chr:
            stack.append(chr)
        else:
            stack.pop()
    return len(stack)


T = int(input())
for test_case in range(T):
    string = input()
    print(f'#{test_case + 1}', len_remainder(string))
