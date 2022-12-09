def main():
    f = open("input/input6.txt", "r")
    lines = f.readlines()
    f.close()
    fish = [int(a) for a in lines[0].split(",") if a != "\n"]
    for _ in range(0, 80):
        new_fish = [(a - 1) % 7 if a < 7 else a - 1 for a in fish]
        for a in fish:
            if a == 0:
                new_fish.append(8)
        fish = new_fish.copy()
    print(len(fish))


def main2():
    f = open("input/input6.txt", "r")
    lines = f.readlines()
    f.close()
    fish = [int(a) for a in lines[0].split(",") if a != "\n"]
    counts = [0] * 9
    for i in fish:
        counts[i] += 1
    for _ in range(0, 1_000_000):
        zeros = counts[0]
        counts.pop(0)
        counts.append(zeros)
        counts[6] += zeros
    print(sum(counts))


if __name__ == '__main__':
    main2()
