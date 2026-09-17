import sys
sys.stdin = open("sample_input.txt", "r")


def last_pizza(N, M, C):
    hwaduck = [None] * N
    current = -1
    next_idx = 0

    while True:
        current = (current + 1) % N

        # 1. 화덕의 현재 위치가 비어있는 경우
        if hwaduck[current] is None:
            if next_idx < M:
                hwaduck[current] = [next_idx, C[next_idx]]
                next_idx += 1

        # 2. 화덕의 현재 위치에 피자가 있는 경우 (들여쓰기 맞춤)
        else:
            hwaduck[current][1] //= 2
            # 치즈가 다 녹은 경우
            if hwaduck[current][1] == 0:
                if next_idx < M:
                    hwaduck[current] = [next_idx, C[next_idx]]
                    next_idx += 1
                else:
                    # 남은 피자가 없으면 빈 공간으로 설정
                    hwaduck[current] = None

        # 3. 종료 조건 검사 (while 내부 위치)
        # hwaduck에서 None이 아닌 진짜 남아있는 피자 객체만 필터링합니다.
        active_pizzas = [p for p in hwaduck if p is not None]

        # 모든 피자를 꺼냈고(next_idx >= M), 화덕에 남은 피자가 1개인 경우
        if len(active_pizzas) == 1 and next_idx >= M:
            return active_pizzas[0][0] + 1  # 남아있는 피자의 1-indexed 번호 반환


T = int(input())
for test_case in range(T):
    N, M = list(map(int, input().split()))
    C = list(map(int, input().split()))
    print(f'#{test_case + 1}', last_pizza(N, M, C))
