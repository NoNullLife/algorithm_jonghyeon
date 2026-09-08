import sys
sys.stdin = open("sample_input.txt", "r")


Map = {
    '}': '{',
    ')': '(',
}

def check_syntex(string):
    stack = []
    for chr in string:
        if chr == '{' or chr == '(':
            stack.append(chr)
        elif chr == '}' or chr == ')':
            if stack == [] or stack[-1] != Map[chr]:
                return 0
            else:
                stack.pop()

    if stack == []:
        return 1
    else:
        return 0


T = int(input())
for test_case in range(T):
    string = input()
    print(f'#{test_case + 1}', check_syntex(string))
