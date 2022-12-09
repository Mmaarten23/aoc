def main():
    lines: list[str] = open('input8.txt', 'r').readlines()
    field: list[list[int]] = [[int(x) for x in line.strip()] for line in lines]

    visible: list[list[bool]] = visible_from_edges(field)

    scenic_score: list[list[int]] = [[0 for _ in range(len(field[0]))] for _ in range(len(field))]
    for i in range(len(field)):
        for j in range(len(field[i])):
            scenic_score[i][j] = visible_from_point(field, i, j)

    part_1: int = sum(visible[i][j] for i in range(len(visible)) for j in range(len(visible[i])))
    part_2: int = max(scenic_score[i][j] for i in range(len(scenic_score)) for j in range(len(scenic_score[i])))
    print(f'Part 1: {part_1}')
    print(f'Part 2: {part_2}')


def visible_from_edges(field: list[list[int]]) -> list[list[bool]]:
    visible: list[list[bool]] = [[False for _ in range(len(field[0]))] for _ in range(len(field))]
    array: list[int]
    for i in range(len(field)):
        array = visible_if_higher(field[i], 0, len(field[i]), 1)
        for j in range(len(field[i])):
            visible[i][j] = visible[i][j] or array[j]
    for i in range(len(field)):
        array = visible_if_higher(field[i], len(field[i]) - 1, -1, -1)
        for j in range(len(field[i])):
            visible[i][j] = visible[i][j] or array[j]
    for i in range(len(field)):
        array = visible_if_higher([row[i] for row in field], 0, len(field), 1)
        for j in range(len(field[i])):
            visible[j][i] = visible[j][i] or array[j]
    for i in range(len(field)):
        array = visible_if_higher([row[i] for row in field], len(field) - 1, -1, -1)
        for j in range(len(field[i])):
            visible[j][i] = visible[j][i] or array[j]
    return visible


def visible_if_higher(row: list[int], start_index: int, end_index: int, step: int) -> list[bool]:
    result: list[bool] = [False for _ in range(len(row))]
    max_row: int = -1
    for i in range(start_index, end_index, step):
        if row[i] > max_row:
            result[i] = True
            max_row = row[i]
    return result


def visible_if_lower(row: list[int]) -> int:
    if len(row) < 1:
        return 0
    max_row: int = row[0]
    result: int = 0
    for i in row[1:]:
        result += 1
        if i >= max_row:
            break
    return result


def visible_from_point(field: list[list[int]], x: int, y: int) -> int:
    visible: int = visible_if_lower(field[x][y:])
    visible *= visible_if_lower([row[y] for row in field[x:]])
    visible *= visible_if_lower(field[x][:y + 1][::-1])
    visible *= visible_if_lower([row[y] for row in field[:x + 1]][::-1])
    return visible


if __name__ == '__main__':
    main()
