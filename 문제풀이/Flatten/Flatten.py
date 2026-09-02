import sys
sys.stdin = open("input.txt", "r")


def find_extream_index(boxes):
    max_value = boxes[0]
    min_value = boxes[0]
    max_index = 0
    min_index = 0

    current_index = 0
    for box in boxes:
        if box > max_value:
            max_value = box
            max_index = current_index

        if box < min_value:
            min_value = box
            min_index = current_index

        current_index += 1

    return max_index, min_index


def dump(boxes):
    max_index, min_index = find_extream_index(boxes)

    dumped_boxes = boxes
    dumped_boxes[max_index] -= 1
    dumped_boxes[min_index] += 1

    return dumped_boxes


T = 10
for test_case in range(T):
    try_dump = int(input())
    boxes = list(map(int, input().split()))

    result = 100  # 상자 높이 차의 최댓값으로 초기화
    for i in range(try_dump):
        boxes = dump(boxes)
        max_index, min_index = find_extream_index(boxes)

        gap = boxes[max_index] - boxes[min_index]
        if gap < result:
            result = gap

        if result == 1:
            break

    print(f'#{test_case + 1}', result)