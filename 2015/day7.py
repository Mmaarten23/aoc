import re


def main():
    lines: list[str] = open('input7.txt', 'r').readlines()
    wires: dict[str, int] = dict()
    calculate_wires(lines, wires)
    a = wires["a"]
    wires.clear()
    lines = [x for x in lines if not re.match(r'\d+ -> b\n', x)]
    lines.append(f'{a} -> b')
    calculate_wires(lines, wires)
    print(f'Part 2: {a}')
    print(f'Part 2: {wires["a"]}')


def calculate_wires(original_lines, wires):
    lines = original_lines
    while not wires.__contains__('a'):
        lines = single_run(lines, wires)


def single_run(lines, wires):
    new_lines = []
    for line in lines:
        try:
            (input1, input2, operator, output) = parse(line.strip(), wires)
        except KeyError:
            new_lines.append(line)
            continue
        match operator:
            case 'ASSIGN':
                wires[output] = input1
            case 'AND':
                wires[output] = input1 & input2
            case 'OR':
                wires[output] = input1 | input2
            case 'LSHIFT':
                wires[output] = input1 << input2
            case 'RSHIFT':
                wires[output] = input1 >> input2
            case 'NOT':
                wires[output] = ~input1
    return new_lines


def parse(command: str, wires: dict):
    tokens: list[str] = command.split()
    if len(tokens) == 3:
        return get_input(tokens[0], wires), None, 'ASSIGN', tokens[-1]
    if tokens[0].isupper():
        return get_input(tokens[1], wires), None, tokens[0], tokens[-1]
    else:
        return get_input(tokens[0], wires), get_input(tokens[2], wires), tokens[1], tokens[-1]


def get_input(input_arg: str, wires: dict) -> int:
    if input_arg.isnumeric():
        return int(input_arg)
    return wires[input_arg]


if __name__ == '__main__':
    main()
