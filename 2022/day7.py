def main():
    text: list[str] = open('input7.txt', 'r').readlines()
    directories, text = parse_commands(text[1:])
    part_1: int = sum([x for x in directories if x <= 100_000])
    part_2: int = sorted([x for x in directories if x > directories[-1] - 40_000_000])[0]
    print(f'Part 1: {part_1}')
    print(f'Part 2: {part_2}')


def parse_commands(commands: list[str]) -> tuple[list[int], list[str]]:
    directories: list[int] = []
    size: int = 0
    while not commands == []:
        tokens, commands = consume_line(commands)
        if tokens[0].isnumeric():
            size += int(tokens[0])
        elif f'{tokens[0]} {tokens[1]}' == '$ cd':
            if tokens[2] == '..':
                return [*directories, size], commands
            new_dirs, commands = parse_commands(commands)
            size += new_dirs[-1]
            directories = [*directories, *new_dirs]
    return [*directories, size], []


def consume_line(text: list[str]) -> tuple[list[str], list[str]]:
    return text[0].split(), text[1:]


if __name__ == '__main__':
    main()
