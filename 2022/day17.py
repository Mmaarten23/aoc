# @formatter:off
import time
blocks: list[list[tuple[int, int]]] = [
    [
        (0, 0), (1, 0), (2, 0), (3, 0)
    ],
    [
                (1, 2),
        (0, 1),         (2, 1),
                (1, 0)
    ],
    [
                        (2, 2),
                        (2, 1),
        (0, 0), (1, 0), (2, 0)
    ],
    [
        (0, 3),
        (0, 2),
        (0, 1),
        (0, 0)
    ],
    [
        (1, 0), (1, 1),
        (0, 0), (0, 1)
    ]
]
# @formatter:on


def main():
    jets: str = open("input/input17.txt").read()
    chute: list[list[str]] = [['.' for _ in range(7)] for _ in range(10_000)]
    current_block_nr: int = 0
    current_jet_nr: int = 0

    current_coords: tuple[int, int] = (2, 3)
    seen = set()
    fall_distance: int = 0
    recurring_state = None
    first_recurring_state = None
    cycle_height: int = 0
    max = 2023
    max = 1_000_000_000_001
    while current_block_nr < max:
        state = (current_block_nr % len(blocks), fall_distance, current_coords[0], current_jet_nr % len(jets), tuple([tuple(x) for x in chute[-10:]]))
        if state in seen and recurring_state is None:
            recurring_state = state
            first_recurring_state = (current_block_nr, get_chute_height(chute) - 1)
            print('Found recurring state')
        elif recurring_state is not None and state == recurring_state and cycle_height == 0:
            print('Found recurring state again')
            print(f'{first_recurring_state[0]} blocks were simulated before the first recurring state was found')
            per_cycle = current_block_nr - first_recurring_state[0]
            print(f'{per_cycle} blocks were simulated since the first recurring state was found')
            left = max - current_block_nr
            print(f'{left} blocks are left to simulate')
            cycles = left // per_cycle
            print(f'{cycles} cycles are left to simulate')
            new_block_nr = first_recurring_state[0] + (cycles + 1) * per_cycle
            print(f'This would bring the amount of simulated blocks to {new_block_nr}')
            current_block_nr = new_block_nr
            cycle_height = (get_chute_height(chute) - 1 - first_recurring_state[1]) * cycles
        else:
            seen.add(state)
        if current_block_nr % 1_000_000 == 0:
            print(f'Block {current_block_nr}')
        current_block: list[tuple[int, int]] = blocks[current_block_nr % len(blocks)]
        current_jet: str = jets[current_jet_nr % len(jets)]
        match current_jet:
            case '>':
                new_coords: tuple[int, int] = (current_coords[0] + 1, current_coords[1])
                if check_move(chute, current_block, new_coords):
                    current_coords = new_coords
            case '<':
                new_coords: tuple[int, int] = (current_coords[0] - 1, current_coords[1])
                if check_move(chute, current_block, new_coords):
                    current_coords = new_coords
            case _:
                raise ValueError(f"Unknown jet: {current_jet}")
        if check_move(chute, current_block, (current_coords[0], current_coords[1] - 1)):
            current_coords = (current_coords[0], current_coords[1] - 1)
            fall_distance += 1
        else:
            for x, y in current_block:
                chute[current_coords[1] + y][current_coords[0] + x] = '#'
            current_block_nr += 1
            current_coords = (2, get_chute_height(chute) + 4)
            fall_distance = 0
        current_jet_nr += 1
    print(cycle_height, get_chute_height(chute) - 1)
    # print(f'Part 1: {trimmed_height * 25 + get_chute_height(chute) - 1}')
    print(f'Part 2: {cycle_height + get_chute_height(chute)}')



def print_chute(chute: list[list[str]], block: list[tuple[int, int]] = None, coords: tuple[int, int] = None):
    chute = [row[:] for row in chute]
    if block and coords:
        for x, y in block:
            chute[coords[1] + y][coords[0] + x] = '@'
    print('|' + ''.join(['-' for _ in range(len(chute[0]))]) + '|')
    # Print chute lines in reverse order. Line 0 and get_chute_height indicate the boundaries
    for y in range(get_chute_height(chute) + 8, -1, -1):
        print('|' + ''.join(chute[y]) + '|')
    print('-' * (len(chute[0]) + 2))


def check_move(chute: list[list[str]], block: list[tuple[int, int]], coords: tuple[int, int]) -> bool:
    for x, y in block:
        new_x, new_y = coords[0] + x, coords[1] + y
        if new_x < 0 or new_x >= len(chute[0]) or new_y < 0 or new_y >= len(chute):
            return False
        if chute[new_y][new_x] != '.':
            return False
    return True


def get_chute_height(chute: list[list[str]]) -> int:
    for y, row in enumerate(chute):
        if not any([c != '.' for c in row]):
            return y - 1


if __name__ == '__main__':
    tic = time.perf_counter()
    main()
    toc = time.perf_counter()
    print(toc - tic)