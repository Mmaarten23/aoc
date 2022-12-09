import re


def main():
    text: str = open('input/input5.txt', 'r').read()
    stack_text, transactions_text = text.split("\n\n")
    stacks_1 = parse_stacks(stack_text)
    stacks_2 = parse_stacks(stack_text)
    transactions = parse_transactions(transactions_text)
    for transaction in transactions:
        (amount, from_stack, to_stack) = transaction
        for _ in range(amount):
            stacks_1[to_stack - 1].append(stacks_1[from_stack - 1].pop())
        stacks_2[to_stack - 1].extend(stacks_2[from_stack - 1][-amount:])
        stacks_2[from_stack - 1] = stacks_2[from_stack - 1][:-amount]
    part_1 = ''
    part_2 = ''
    for stack in stacks_1:
        part_1 += ''.join(stack.pop())
    for stack in stacks_2:
        part_2 += ''.join(stack.pop())
    print(f'Part 1: {part_1}')
    print(f'Part 2: {part_2}')



def parse_stacks(stack_text: str) -> list[list[str]]:
    lines: list[str] = stack_text.split("\n")
    amount: int = (len(lines[0]) + 1) // 4
    stacks = [[] for _ in range(amount)]
    for line in lines[:-1]:
        for i in range(amount):
            elem = line[1 + i * 4]
            if elem != ' ':
                stacks[i].insert(0, elem)
    return stacks


def parse_transactions(transactions_text: str) -> list[tuple[int, int, int]]:
    transactions = []
    for line in transactions_text.split('\n'):
        if line == '':
            continue
        match = re.match(r'move (\d+) from (\d+) to (\d+)', line)
        if match is None:
            raise ValueError(f'Invalid transaction: {line}')
        transactions.append((int(match.group(1)), int(match.group(2)), int(match.group(3))))
    return transactions



if __name__ == '__main__':
    main()
