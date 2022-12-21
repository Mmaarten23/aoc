import re
import threading


def main():
    lines: list[str] = [line.strip() for line in open("input/input21.txt", 'r').readlines()]
    print(f'Part 1: {part_1(lines.copy())}')
    print(f'Part 2: {part_2(lines.copy())}')


def part_1(lines):
    var = vars()
    for line in lines.copy():
        match = re.match(r'(\w+): (\d+)', line)
        if match:
            var[match.group(1)] = int(match.group(2))
            lines.remove(line)
    while not var.__contains__('root'):
        for line in lines.copy():
            match = re.match(r'(\w+): (.*)', line)
            if not match:
                raise ValueError("Invalid line " + line)
            try:
                var[match.group(1)] = eval(match.group(2))
                lines.remove(line)
            except NameError:
                continue
    return int(var['root'])


def part_2(l):
    N = 100_000_000
    nb = 100
    step = N / nb
    ranges = [range(round(step*i), round(step*(i+1))) for i in range(nb)]
    for r in ranges:
        threading.Thread(target=run_range, args=(r, l)).start()


def run_range(r, l):
    for human in r:
        lines = l.copy()
        var = vars()
        var['humn'] = human
        for line in lines.copy():
            match = re.match(r'(\w+): (\d+)', line)
            if match:
                if match.group(1) == 'humn':
                    continue
                var[match.group(1)] = int(match.group(2))
                lines.remove(line)
        while not var.__contains__('root'):
            for line in lines.copy():
                match = re.match(r'(\w+): (.*)', line)
                if not match:
                    raise ValueError("Invalid line " + line)
                string = match.group(2) if match.group(1) != 'root' else match.group(2).replace('+', '==')
                try:
                    var[match.group(1)] = eval(string)
                    lines.remove(line)
                except NameError:
                    continue
        if var['root']:
            print(human)
        var.clear()


if __name__ == '__main__':
    main()
