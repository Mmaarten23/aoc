def main():
    text: str = open('input/input11.txt', 'r').read()
    monkeys: dict[int, dict[str, list[int] | str | int]] = parse(text)

    # for _ in range(20):
    for _ in range(10000):
        for monkey_nr in range(len(monkeys)):
            monkey = monkeys[monkey_nr]
            for old in monkey['items']:
                monkey['inspections'] += 1
                new: int = eval(monkey['operation'])
                # worry = new // 3
                worry = new
                if worry % monkey['test'] == 0:
                    # monkeys[monkey['true']]['items'].append(worry)
                    monkeys[monkey['true']]['items'].append(worry % 9699690)
                else:
                    # monkeys[monkey['false']]['items'].append(worry)
                    monkeys[monkey['false']]['items'].append(worry % 9699690)
            monkey['items'].clear()
    inspections: list[int] = sorted([monkeys[monkey]['inspections'] for monkey in range(len(monkeys))])
    # print(f'Part 1: {inspections[-1] * inspections[-2]}')
    print(f'Part 2: {inspections[-1] * inspections[-2]}')


def parse(text: str) -> dict[int, dict[str, list[int] | str | int]]:
    monkeys: dict[int, dict[str, list[int] | str | int]] = {}
    monkeys_t: list[str] = text.split('\n\n')
    for i in range(len(monkeys_t)):
        tokens: list[str] = monkeys_t[i].split('\n')
        monkeys[i] = {}
        monkeys[i]['items'] = [int(x) for x in tokens[1][18:].split(',')]
        monkeys[i]['operation'] = tokens[2][19:]
        monkeys[i]['test'] = int(tokens[3][21:])
        monkeys[i]['true'] = int(tokens[4][29:])
        monkeys[i]['false'] = int(tokens[5][30:])
        # Add default counter
        monkeys[i]['inspections'] = 0
    return monkeys


if __name__ == '__main__':
    main()
