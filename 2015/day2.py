def main():
    lines: list[str] = open('input/input2.txt').readlines()
    part_1: int = 0
    part_2: int = 0
    for line in lines:
        l, w, h = [int(x) for x in line.strip().split('x')]
        part_1 += 2 * l * w + 2 * w * h + 2 * h * l + min(l * w, w * h, h * l)
        small_1 = min(l, w, h)
        small_2 = sorted([l, w, h])[1]
        part_2 += small_1 + small_1 + small_2 + small_2 + l * w * h

    print(f'Part 1: {part_1}')
    print(f'Part 2: {part_2}')


if __name__ == '__main__':
    main()
