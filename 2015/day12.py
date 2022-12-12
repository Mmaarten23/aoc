import json
import re


def main():
    old: str = open('input/input12.txt', 'r').read()
    numbers: list[int] = [int(x) for x in re.findall(r'(-?\d+)\D', old)]

    parsed = json.loads(old)
    new = sum_numbers(parsed)

    print(f'Part 1: {sum(numbers)}')
    print(f'Part 2: {new}')


def sum_numbers(parsed):
    if isinstance(parsed, int):
        return parsed
    if isinstance(parsed, list):
        return sum(sum_numbers(x) for x in parsed)
    if isinstance(parsed, dict):
        if 'red' in parsed.values():
            return 0
        return sum(sum_numbers(x) for x in parsed.values())
    return 0


if __name__ == '__main__':
    main()
