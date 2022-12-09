import re


def main():
    line: str = open('input/input10.txt').read().strip()
    print(f'Part 1: {len(run(line, 40))}')
    print(f'Part 2: {len(run(line, 50))}')


def run(line:str, times: int) -> str:
    for i in range(times):
        split: list[str] = [x[0] for x in re.findall(r'((\d)\2*)', line)]
        line = ''
        for j in split:
            line += str(len(j)) + j[0]
    return line


if __name__ == '__main__':
    main()
