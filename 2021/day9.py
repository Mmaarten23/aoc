import math


def main():
    f = open("input/input9.txt", "r")
    lines = f.readlines()
    f.close()
    risk = 0
    heightmap = [[int(char) for char in line.replace("\n", "")] for line in lines]
    for i in range(0, len(heightmap)):
        for j in range(0, len(heightmap[0])):
            value = heightmap[i][j]
            smallest = True
            if i > 0 and heightmap[i - 1][j] <= value:
                smallest = False
            if i < len(heightmap) - 1 and heightmap[i + 1][j] <= value:
                smallest = False
            if j > 0 and heightmap[i][j - 1] <= value:
                smallest = False
            if j < len(heightmap[0]) - 1 and heightmap[i][j + 1] <= value:
                smallest = False
            if smallest:
                risk += value + 1
    print(risk)


def main2():
    f = open("input/input9.txt", "r")
    lines = f.readlines()
    f.close()
    heightmap = [[int(char) for char in line.replace("\n", "")] for line in lines]
    basins = []
    for i in range(0, len(heightmap)):
        for j in range(0, len(heightmap[0])):
            value = heightmap[i][j]
            smallest = True
            if i > 0 and heightmap[i - 1][j] <= value:
                smallest = False
            if i < len(heightmap) - 1 and heightmap[i + 1][j] <= value:
                smallest = False
            if j > 0 and heightmap[i][j - 1] <= value:
                smallest = False
            if j < len(heightmap[0]) - 1 and heightmap[i][j + 1] <= value:
                smallest = False
            if smallest:
                basins.append([[i, j]])
    modified = True
    while modified:
        modified = False
        for basin in basins:
            for i in range(0, len(heightmap)):
                for j in range(0, len(heightmap[0])):
                    value = [i, j]
                    if heightmap[i][j] != 9:
                        adding = False
                        if i > 0 and basin.__contains__([i - 1, j]):
                            adding = True
                        if i < len(heightmap) - 1 and basin.__contains__([i + 1, j]):
                            adding = True
                        if j > 0 and basin.__contains__([i, j - 1]):
                            adding = True
                        if j < len(heightmap[0]) - 1 and basin.__contains__([i, j + 1]):
                            adding = True
                        if adding and not basin.__contains__(value):
                            basin.append([i, j])
                            modified = True
    sizes = [len(basin) for basin in basins]
    sizes.sort()
    sizes.reverse()
    print(math.prod(sizes[0:3]))


if __name__ == '__main__':
    main2()
