import math


def part1(instructions: list[str], nodes: dict[str, tuple[str, str]]) -> int:
    i: int = 0
    current_node: str = 'AAA'
    while current_node != 'ZZZ':
        if instructions[i % len(instructions)] == 'L':
            current_node = nodes[current_node][0]
        else:
            current_node = nodes[current_node][1]
        i += 1
    return i


def part2(instructions: list[str], nodes: dict[str, tuple[str, str]]) -> int:
    start_nodes: list[str] = [x for x in nodes.keys() if x[-1] == 'A']
    current_nodes: list[str] = start_nodes.copy()
    i: int = 0
    first_times: list[int] = [0] * len(current_nodes)
    while 0 in first_times:
        for j in range(len(current_nodes)):
            if instructions[i % len(instructions)] == 'L':
                current_nodes[j] = nodes[current_nodes[j]][0]
            else:
                current_nodes[j] = nodes[current_nodes[j]][1]
            if current_nodes[j][-1] == 'Z':
                if first_times[j] == 0:
                    first_times[j] = i + 1
        i += 1
    print(math.lcm(*first_times))


def main():
    with open('input/day8.txt') as f:
        lines = f.read().splitlines()
    instructions: list[str] = [x for x in lines[0]]
    nodes: dict[str, tuple[str, str]] = {}
    for i in range(2, len(lines)):
        values: str = ""
        key, values = lines[i].split(' = ')
        left, right = values[1: -1].split(', ')
        nodes[key] = (left, right)
    # print(part1(instructions, nodes))
    print(part2(instructions, nodes))


if __name__ == '__main__':
    main()
