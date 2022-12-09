def main():
    text: str = open('input/input1.txt', 'r').read()
    sums: list[int] = sorted(get_sums(text), reverse=True)
    print(f'Part 1: {sums[0]}')
    print(f'Part 2: {sum(sums[:3])}')


def get_sums(text: str) -> list[int]:
    return [sum([int(calorie) for calorie in calories.split('\n')]) for calories in text.split("\n\n")]


if __name__ == '__main__':
    main()
