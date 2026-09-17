import sys
sys.stdin = open("sample_input.txt", "r")


def Pascal_tri(row,col):
    M = [[1]*(row+1) for _ in range(row+1)]
    for i in range(row+1):
        for j in range(1,i):
            M[i][j] = M[i-1][j-1] + M[i-1][j]

    return M[row][col]


def count_case(N):
    N //= 10
    q = N // 2
    r = N % 2
    case_cnt = 0
    for num_of_size_20 in range(q+1):
        num_of_size_10 = N - 2 * num_of_size_20
        total_num = num_of_size_10 + num_of_size_20

        # 2칸짜리 x개와 1칸짜리 y개를 놓는다고 하자. x+y개의 자리들 중 2칸짜리가 들어갈 자리 x개를 고른다.
        # x+yCx를 파스칼 삼각형을 이용하여 구한 뒤,
        # 2칸짜리는 가로로 분할될 수 있으니, 2칸짜리 개수만큼 2를 곱해준다.
        # 세로로 분할되는 경우는 1칸짜리 2개를 세팅한 것과 같으므로 중복으로 세지 않는다.
        case_cnt += Pascal_tri(total_num, num_of_size_20) * 2**num_of_size_20

    return case_cnt


T = int(input())
for test_case in range(T):
    N = int(input())
    print(f'#{test_case + 1}', count_case(N))
