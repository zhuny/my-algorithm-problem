import collections
import heapq
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


def solution_large(closing: int, running: int, lunch: int, starts: List[int]):
    class DirectGraph:
        def __init__(self):
            self.edge = collections.defaultdict(dict)
            self.vertex = {False: set(), True: set()}

        def add_edge(self, source, target, weight):
            self.edge[source][target] = weight
            self.vertex[source[1]].add(source)
            self.vertex[target[1]].add(target)

        def get_vertex(self, is_eat):
            vertex = list(self.vertex[is_eat])
            vertex.sort()
            return vertex

        def is_connect(self, source, target):
            return (
                source in self.edge and
                target in self.edge[source]
            )

        def get_shortest(self, v1, v2):
            heap = [(0, v1)]
            length_min = {v1: 0}

            while heap:
                length, source = heapq.heappop(heap)
                if source == v2:
                    return length

                if source in self.edge:
                    for target, weight in self.edge[source].items():
                        if target not in length_min or length_min[target] > length+weight:
                            length_min[target] = length+weight
                            heapq.heappush(heap, (length+weight, target))

    def conti(iteration):
        before = []
        for i in iteration:
            before.append(i)
            if len(before) == 2:
                yield before[0], before[1]
                before.pop(0)

    # vertex를 (시간, 밥을 먹었나) 튜플로 두고,
    # edge의 weight를 어떠한 행동도 하지 않은 시간으로 둔다.
    # 밥을 먹거나 영화를 볼 때에는 행동을 취한 것이므로 weight가 0이지만
    # 영화 사이사이 비는 시간에는 행동도 하지 않으므로 두 vertex간의 시간 차이가 weight가 된다
    graph = DirectGraph()
    graph.add_edge(
        (0, False), (lunch, True),  # 극장에 오자마자 밥을 먹은 경우
        0
    )
    graph.add_edge(
        (closing-lunch, False), (closing, True),  # 극장이 끝나기 전에 밥을 먹는 경우
        0
    )

    for start in starts:
        graph.add_edge(
            (start, False), (start+running, False),  # 밥을 먹지 않은 상태에서 영화를 봄
            0
        )
        graph.add_edge(
            (start, True), (start+running, True),  # 밥을 먹은 상태에서 영화를 봄
            0
        )
        graph.add_edge(
            (start+running, False), (start+running+lunch, True),  # 이번 영화를 보고 밥을 먹으러 가는 경우
            0
        )

    for is_eat in [False, True]:
        for before, after in conti(graph.get_vertex(is_eat)):
            if not graph.is_connect(before, after):
                graph.add_edge(before, after, after[0]-before[0])  # 밥을 먹은 상태에서 사이사이 시간이 비었을 때

    shortest = graph.get_shortest(
        (0, False),      # 시간 0, 밥을 먹지 않은 상태
        (closing, True)  # 시간이 closing, 밥을 먹은 상태
    )
    # closing-shortest 값이 lunch + running * {영화를 본 횟수}
    assert (closing-shortest-lunch) % running == 0
    return (closing-shortest-lunch) // running


if __name__ == '__main__':
    import random

    def run(closing: int, running: int, lunch: int, starts: List[int], sol: int):
        print(
            solution_small(closing, running, lunch, starts),
            solution_large(closing, running, lunch, starts),
            sol
        )

    run(5, 5, 3, [0], 0)
    run(12, 3, 5, [0, 3, 6, 9], 2)
    run(24, 10, 4, [0, 7, 14], 2)

    def generate_random():
        N = 1_000_000_000 - 100_000
        gen = {random.randint(0, N) for i in range(20000)}
        gen = list(gen)
        gen.sort()
        return gen


    print(solution_large(
        1_000_000_000,
        100_000,
        50_000,
        generate_random()
    ))


