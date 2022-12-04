def main():
    lines: list[str] = open('input4.txt', 'r').readlines()
    count: int = 0
    count2: int = 0
    for line in lines:
        elf1_range, elf2_range = range_from_line(line)
        inter: range = intersect(elf1_range, elf2_range)
        if len(inter) == len(elf1_range) or len(inter) == len(elf2_range):
            count += 1
        if len(inter) > 0:
            count2 += 1

    print(f'Part 1: {count}')
    print(f'Part 2: {count2}')


def range_from_line(line):
    return [range(int(elf.split('-')[0]), int(elf.split('-')[1]) + 1) for elf in line.strip().split(',')]


def intersect(r1: range, r2: range) -> range:
    return range(max(r1.start, r2.start), min(r1.stop, r2.stop))


if __name__ == '__main__':
    main()
