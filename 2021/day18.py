import pathlib
import sys

from typing import Union

sys.path.append(str(pathlib.Path(__file__).resolve().parent.parent / 'lib'))

class Number:
    def __init__(self, n: int) -> None:
        self.val = n
        self.prev = None
        self.next = None

    def __str__(self) -> str:
        return str(self.val)

    def magnitude(self) -> int:
        return self.val


class Pair:
    @classmethod
    def add(cls: str, pair1: 'Pair', pair2: 'Pair') -> 'Pair':
        pair = Pair(0)

        pair1.reduce()
        pair2.reduce()

        pair1.increase_depth()
        pair2.increase_depth()

        last = pair1.last()
        first = pair2.first()
        last.next = first
        first.prev = last

        pair.left = pair1
        pair.right = pair2
        pair.reduce()

        return pair


    def __init__(self, depth: int) -> None:
        self.depth = depth
        self.left: Union[Number,Pair] = None
        self.right: Union[Number,Pair] = None

    def __str__(self) -> str:
        return "[" + str(self.left) + "," + str(self.right) + "]"

    def __explode_step(self) -> bool:
        if isinstance(self.left, Pair):
            if self.left.depth >= 4:
                if self.left.left.prev:
                    self.left.left.prev.val += self.left.left.val

                if self.left.right.next:
                    self.left.right.next.val += self.left.right.val

                num = Number(0)
                num.prev = self.left.left.prev
                num.next = self.left.right.next
                if num.prev:
                    num.prev.next = num
                if num.next:
                    num.next.prev = num

                self.left = num
                return True

            elif self.left.__explode_step():
                return True

        if isinstance(self.right, Pair):
            if self.right.depth >= 4:
                if self.right.left.prev:
                    self.right.left.prev.val += self.right.left.val

                if self.right.right.next:
                    self.right.right.next.val += self.right.right.val

                num = Number(0)
                num.prev = self.right.left.prev
                num.next = self.right.right.next
                if num.prev:
                    num.prev.next = num
                if num.next:
                    num.next.prev = num

                self.right = num
                return True

            elif self.right.__explode_step():
                return True

        return False

    def __split_step(self: 'Pair') -> bool:
        if isinstance(self.left, Pair):
            if self.left.__split_step():
                return True

        if isinstance(self.left, Number):
            if self.left.val >= 10:
                pair = Pair(self.depth + 1)
                pair.left = Number(self.left.val // 2)
                pair.right = Number(int(self.left.val / 2 + 0.5))

                pair.left.next = pair.right
                pair.right.prev = pair.left

                if self.left.prev:
                    pair.left.prev = self.left.prev
                    pair.left.prev.next = pair.left

                if self.left.next:
                    pair.right.next = self.left.next
                    pair.right.next.prev = pair.right

                self.left = pair
                return True

        if isinstance(self.right, Pair):
            if self.right.__split_step():
                return True

        if isinstance(self.right, Number):
            if self.right.val >= 10:
                pair = Pair(self.depth + 1)
                pair.left = Number(self.right.val // 2)
                pair.right = Number(int(self.right.val / 2 + 0.5))

                pair.left.next = pair.right
                pair.right.prev = pair.left

                if self.right.prev:
                    pair.left.prev = self.right.prev
                    pair.left.prev.next = pair.left

                if self.right.next:
                    pair.right.next = self.right.next
                    pair.right.next.prev = pair.right

                self.right = pair
                return True

        return False

    def reduce(self) -> None:
        while self.__explode_step() or self.__split_step():
            pass

    def increase_depth(self) -> None:
        self.depth += 1
        if isinstance(self.left, Pair):
            self.left.increase_depth()
        if isinstance(self.right, Pair):
            self.right.increase_depth()

    def first(self) -> 'Pair':
        if isinstance(self.left, Number):
            return self.left
        else:
            return self.left.first()

    def last(self) -> 'Pair':
        if isinstance(self.right, Number):
            return self.right
        else:
            return self.right.last()

    def magnitude(self) -> int:
        return self.left.magnitude() * 3 + 2 * self.right.magnitude()


def read_number(number: str) -> Pair:
    pairs = []
    depth = 0
    val = 0
    is_val = False
    node = None
    prev = None

    for c in number:
        if c == '[':
            pairs.append(Pair(depth))
            depth += 1

        elif c == ']':
            if is_val:
                pairs[-1].right = prev
                is_val = False
            else:
                pairs[-1].right = node

            node = pairs.pop()
            depth -= 1

        elif c == ',':
            if is_val:
                pairs[-1].left = prev
                is_val = False
            else:
                pairs[-1].left = node

        else:
            if not is_val:
                node = Number(0)
                if prev:
                    prev.next = node
                    node.prev = prev
                prev = node
                is_val = True

            node.val = node.val * 10 + int(c)

    return node


def run() -> None:
    lines = [l.strip() for l in open('input/input18.txt').readlines()]

    summed = read_number(lines[0])
    for line in lines[1:]:
        summed = Pair.add(summed, read_number(line))
    print(f'Magnitude of total sum: {summed.magnitude()}')

    max_magnitude = 0
    for idx1 in range(len(lines)):
        for idx2 in range(len(lines)):
            if idx1 == idx2:
                continue

            summed = Pair.add(read_number(lines[idx1]), read_number(lines[idx2]))
            max_magnitude = max(max_magnitude, summed.magnitude())
    print(f'Max magnitude of any two sums: {max_magnitude}')


if __name__ == '__main__':
    run()
    sys.exit(0)