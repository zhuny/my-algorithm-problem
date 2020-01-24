from dataclasses import dataclass
from typing import List


class Block:
    def __init__(self, pos, name, cycle):
        self.pos: List[Pos] = pos
        self.name = name
        self.cycle = cycle

    def rotate(self):
        pos = [p.rotate() for p in self.pos]
        x_list, y_list = zip(*[p.key() for p in pos])
        offset = Pos(-min(x_list), -min(y_list))
        self.pos = [
            p+offset
            for p in pos
        ]

    @staticmethod
    def alphabet(string):
        for char in string:
            if char.strip():
                return char

    @classmethod
    def from_string(cls, string, cycle):
        name = cls.alphabet(string)
        pos = []
        for i, line in enumerate(string.splitlines()):
            for j, char in enumerate(line):
                if name == char:
                    pos.append(Pos(i, j))
        return cls(pos, name, cycle)

    def with_offset(self, offset):
        for pos in self.pos:
            yield pos+offset

    def valid_pos(self, plate, offset):
        for pos in self.with_offset(offset):
            if pos.key() not in plate:
                return False
        return True


@dataclass
class Pos:
    x: int
    y: int

    def __add__(self, other):
        return Pos(self.x+other.x, self.y+other.y)

    def key(self):
        return self.x, self.y

    def rotate(self):
        return Pos(self.y, -self.x)


class State:
    def __init__(self):
        self.block_pos = []

    def put_block(self, plate, block, offset):
        for pos in block.with_offset(offset):
            plate.remove(pos.key())
        self.block_pos.append((block, offset))

    def back_block(self, plate, block, offset):
        for pos in block.with_offset(offset):
            plate.add(pos.key())
        self.block_pos.pop()

    def show(self):
        d = {}
        for block, offset in self.block_pos:
            for pos in block.with_offset(offset):
                d[pos.key()] = block.name

        x_list, y_list = zip(*d)
        x_max, y_max = max(x_list)+1, max(y_list)+1

        for i in range(x_max):
            print("".join(d.get((i, j), " ") for j in range(y_max)))
        print()


def valid_position(plate, block):
    x_pos = []
    y_pos = []
    for x, y in plate:
        x_pos.append(x)
        y_pos.append(y)
    x_min, x_max = min(x_pos), max(x_pos)
    y_min, y_max = min(y_pos), max(y_pos)
    for x in range(x_min, x_max+1):
        for y in range(y_min, y_max+1):
            offset = Pos(x, y)
            if block.valid_pos(plate, offset):
                yield offset


def travel_block(plate, blocks, index, state):
    if index == len(blocks):
        yield state
        return

    for i in range(blocks[index].cycle):
        for pos in valid_position(plate, blocks[index]):
            state.put_block(plate, blocks[index], pos)
            yield from travel_block(plate, blocks, index+1, state)
            state.back_block(plate, blocks[index], pos)
        blocks[index].rotate()


def create_blocks():
    blocks = [
        ("IIII", 2),      # block I
        ("OO\nOO", 1),    # block O
        ("TTT\n T", 4),   # block T
        ("JJ\nJ\nJ", 4),  # block J
        ("LLL\nL", 4),    # block L
        (" SS\nSS", 2),   # block S
        ("ZZ\n ZZ", 2),   # block Z
    ]
    return [
        Block.from_string(block, cycle)
        for block, cycle in blocks
    ]


def travel_every_block():
    plate = {
        (i, j)
        for i in range(6)
        for j in range(max(1-i, i-2), 7-max(1-i, i-2))
    }
    assert len(plate) >= 28
    blocks = create_blocks()

    for state in travel_block(plate, blocks, 0, State()):
        yield state


def solution(N: int):
    for state in travel_every_block():
        state.show()
        N -= 1
        if N == 0:
            break


if __name__ == '__main__':
    solution(100000000)


