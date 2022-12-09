import re


def main():
    original: list[str] = open('input/input8.txt').read().splitlines()
    lines: list[str] = original.copy()
    code: list[int] = [len(x) for x in lines]
    lines = [line.replace('\\"', '#') for line in lines]
    lines = [line.replace('\\\\', '#') for line in lines]
    lines = [re.sub(r'\\x..', '#', line) for line in lines]
    lines = [line[1:-1] for line in lines]
    memory: list[int] = [len(x) for x in lines]

    lines_2: list[str] = original.copy()
    lines_2 = [line.replace('\\', '\\\\') for line in lines_2]
    lines_2 = [line.replace('"', r'\"') for line in lines_2]
    lines_2 = ['"' + line + '"' for line in lines_2]
    memory_2: list[int] = [len(x) for x in lines_2]

    print(f'Part 1: {sum(code) - sum(memory)}')
    print(f'Part 2: {sum(memory_2) - sum(code)}')


if __name__ == '__main__':
    main()
