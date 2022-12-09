def main():
    f = open('input/input17.txt', "r")
    x, y = [b for b in
            f.readline().replace("\n", "").replace("target area: ", "").replace("x=", "").replace("y=", "").split(", ")]
    minx, maxx = [int(a) for a in x.split("..")]
    miny, maxy = [int(a) for a in y.split("..")]
    f.close()

    max_height = 0
    for x in range(maxx + 1):
        for y in range(0, 500):
            new_height = calculateMaxY([minx, maxx, miny, maxy], x, y)
            if new_height > max_height:
                max_height = new_height

    print(max_height)


def main2():
    f = open('input/input17.txt', "r")
    x, y = [b for b in
            f.readline().replace("\n", "").replace("target area: ", "").replace("x=", "").replace("y=", "").split(", ")]
    minx, maxx = [int(a) for a in x.split("..")]
    miny, maxy = [int(a) for a in y.split("..")]
    f.close()
    count = 0
    for x in range(maxx + 1):
        for y in range(-500, 500):
            if hits([minx, maxx, miny, maxy], x, y):
                count += 1
    print(count)


def calculateMaxY(region, vx, vy):
    maxy = 0
    x = y = 0
    while x <= region[1] and y >= region[3]:
        x += vx
        y += vy
        vx = max(0, vx - 1)
        vy -= 1
        maxy = max(maxy, y)
        if region[0] <= x <= region[1] and region[2] <= y <= region[3]:
            return maxy
    return 0


def hits(region, vx, vy):
    x = y = 0
    while x <= region[1] + 150 and y >= region[3] - 150:
        x += vx
        y += vy
        vx = max(0, vx - 1)
        vy -= 1
        if region[0] <= x <= region[1] and region[2] <= y <= region[3]:
            return True
    return False


if __name__ == '__main__':
    main2()
