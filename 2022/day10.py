def main():
    lines: list[str] = open('input/input10.txt', 'r').readlines()
    line_nr: int = 0
    cooldown: bool = False
    buffer: int = 0
    signal: int = 0
    x: int = 1
    screen: list[list[str]] = [[' ' for _ in range(40)] for _ in range(6)]
    for cycle in range(1, 240):
        if cycle in [20, 60, 100, 140, 180, 220]:
            signal += cycle * x

        if abs((cycle - 1) % 40 - x) <= 1:
            screen[(cycle - 1) // 40][(cycle - 1) % 40] = '#'

        if cooldown:
            cooldown = False
            x += buffer
            continue

        line: str = lines[line_nr].strip()
        line_nr += 1
        if line == 'noop':
            continue

        amount: int = int(line.split()[1])
        buffer = amount
        cooldown = True

    print(f'Part 1: {signal}')
    print(f'Part 2:')
    for line in screen:
        print(''.join(line))


if __name__ == '__main__':
    main()
