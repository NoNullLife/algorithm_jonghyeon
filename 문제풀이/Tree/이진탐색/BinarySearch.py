import sys
sys.stdin = open("sample_input.txt", "r")

"""
DFS 가지치기로 풀면 쉽게 해결할 수 있지 않을까...?
-----------------------------------------------------------
ㄴㄴㄴㄴㄴ 절대안됨. 훨씬 느려짐.
중위순회 방식(왼-루트-오 순)으로 가야한다.
-----------------------------------------------------------
def in_order(T):
if T:   # 0이 아니면 (존재하는 정점이면)
    in_order(left[T])  # 왼쪽 자식(서브트리)로 이동
    print(T)  # visit(T) T에서 할일 처리
    in_order(right[T]) # 오른쪽 자식(서브트리)로 이동
-----------------------------------------------------------
"""


def in_order(N, tree, current_node, current_val):
    if current_node > N:
        return current_val, tree

    # 1. 왼쪽 서브트리 순회
    current_val, tree = in_order(N, tree, 2 * current_node, current_val)

    # 2. 현재 노드에 값 채우기
    tree[current_node] = current_val
    current_val += 1

    # 3. 오른쪽 서브트리 순회
    current_val, tree = in_order(N, tree, 2 * current_node + 1, current_val)

    # 루트 노드(1번)인 경우, 최종 결과 문구 반환 / 그 외는 상태(val, tree) 반환
    if current_node == 1:
        return f"{tree[1]} {tree[N // 2]}"

    return current_val, tree


T = int(input())
for test_case in range(T):
    N = int(input())
    tree = [0] * (N + 1)
    print(f'#{test_case + 1}', in_order(N, tree, 1, 1))
