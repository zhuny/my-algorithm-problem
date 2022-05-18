import collections
from typing import List, Dict


class SolutionSmall:
    def build_graph(self, edge_list) -> Dict[int, List[int]]:
        graph = collections.defaultdict(list)
        for v1, v2 in edge_list:
            graph[v1].append(v2)
            graph[v2].append(v1)
        return graph

    def travel_path(self, start, end, graph) -> List[int]:
        # start에서 퍼지는 prev_map 구성하기
        prev_map = {start: start}
        queue = [(start, start)]  # which means no root
        while queue:
            prev, current = queue.pop()
            if current == end:
                break
            for next_v in graph[current]:
                if next_v == prev:
                    continue
                prev_map[next_v] = current
                queue.append((current, next_v))

        # path 찾기
        current = end
        path = [current]
        while current != start:
            current = prev_map[current]
            path.append(current)
        path.reverse()
        return path

    def solve(self,
              x_start: int, x_end: int,
              y_start: int, y_end: int,
              edge_list: List[List[int]]):
        g = self.build_graph(edge_list)
        x_path = set(self.travel_path(x_start, x_end, g))
        y_path = set(self.travel_path(y_start, y_end, g))
        return len(x_path.intersection(y_path))


def main():
    assert SolutionSmall().solve(
        0, 3,
        4, 5,
        [[0, 1], [1, 2], [2, 3], [4, 1], [2, 5]]
    ) == 2, "Case 1"
    assert SolutionSmall().solve(
        0, 4,
        3, 5,
        [[0, 1], [1, 2], [2, 3], [4, 1], [2, 5]]
    ) == 0, "Case 2"


if __name__ == '__main__':
    main()
