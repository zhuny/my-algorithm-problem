from typing import List


def solution_small(closing: int, running: int, lunch: int, starts: List[int]):
    start_time = set(starts)

    # 밥과 상관없이 최대 갯수
    max_before = []
    max_count_before = 0
    for i in range(closing+1):
        if i-running in start_time:
            max_count_before = max(max_count_before, max_before[i-running]+1)
        max_before.append(max_count_before)

    # 밥을 언제 먹으면 좋을까
    max_after = [-1] * lunch  # 이 시간 동안은 밥도 못 먹는다.
    max_count_after = 0
    for i in range(lunch, closing+1):
        max_count_after = max(max_count_after, max_before[i-lunch])
        if running <= i and max_after[i-running] != -1:
            max_count_after = max(max_count_after, max_after[i-running]+1)
        max_after.append(max_count_after)

    return max_after[closing]


if __name__ == '__main__':
    print(solution_small(5, 5, 3, [0]), 0)
    print(solution_small(12, 3, 5, [0, 3, 6, 9]), 2)
    print(solution_small(24, 10, 4, [0, 7, 14]), 2)


