import re
from re import Match


def main():
    lines: list[str] = open('input/input13.txt', 'r').readlines()
    values: dict[str, int] = parse(lines)
    names: list[str] = list(set([key.split()[0] for key in values.keys()]))

    p: list[str] = permutations(len(names), names)
    scores: list[int] = [get_score(values, x) for x in p]

    names.append('Maarten')
    p_2: list[str] = permutations(len(names), names)
    scores_2: list[int] = [get_score(values, x) for x in p_2]

    print(f'Part 1: {max(scores)}')
    print(f'Part 2: {max(scores_2)}')


def parse(text: list[str]) -> dict[str, int]:
    result: dict = dict()
    for line in text:
        match: Match = re.match(r'(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+)\.', line)
        result[f'{match.group(1)} {match.group(4)}'] = int(match.group(3)) * (1 if match.group(2) == 'gain' else -1)
    return result


def permutations(length: int, original: list[str]) -> list[str]:
    if length == 0:
        return ['']
    recursive = permutations(length - 1, original)
    result: list[str] = []
    for o in original:
        for r in recursive:
            if r.find(o) == -1:
                result.append(f'{o} {r}' if r != '' else o)
    return result


def get_score(values: dict[str, int], x: str) -> int:
    tokens: list[str] = x.split()
    score: int = 0
    for i in range(len(tokens)):
        try:
            score += values[f'{tokens[i]} {tokens[(i + 1) % len(tokens)]}']
        except KeyError:
            pass
        try:
            score += values[f'{tokens[(i + 1) % len(tokens)]} {tokens[i]}']
        except KeyError:
            pass
    return score


if __name__ == '__main__':
    main()
