def generate_power_set(L):
    n = len(L)          # 집합의 크기
    power_set = []      # 부분집합들을 담을 리스트

    for d in range(2 ** n):     # 0번째부터 2^n-1번째까지 중
        subset = []             # d번째 부분집합을 만들 리스트
        idx = 0                 # enumerate 대신 idx = 0 사용

        # 핵심! 비트연산자 안쓰고 내장함수 bin으로 이진수 문자열을 얻는다.
        # 0,1번째 문자는 필요가 없다. 또한, 자릿수 문제로 중복이 발생할 수 있으므로 reverse시킨다.
        # 이진수니깐 trigger는 0아니면 1이다.
        for trigger in list(map(int, bin(d)[-1:1:-1])):
            if trigger:
                subset.append(L[idx])   # trigger가 1이면 해당 인덱스에 해당하는 L의 원소를 추가한다.
            idx += 1                    # 0이면 그냥 넘어가되, 값에 상관없이 idx는 계속 업데이트해준다.

        # 완성된 부분집합을 멱집합에 추가한다.
        power_set.append(subset)

    # 완성된 멱집합을 반환한다.
    return power_set


L = [1, 2, 3, 4]
print(generate_power_set(L))
