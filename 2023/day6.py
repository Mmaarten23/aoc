def calculate_distances(time: int) -> list[int]:
    distances: list[int] = [0] * time
    for i in range(time):
        distances[i] = i * (time - i)
    return distances


def part1(times, distances):
    solution: int = 1
    for time_index in range(len(times)):
        time: int = times[time_index]
        new_distances: list[int] = calculate_distances(time)
        count: int = 0
        for distance in new_distances:
            if distance > distances[time_index]:
                count += 1
        solution *= count
    return solution


def part2(times: list[int], distances: list[int]) -> int:
    time: str = ''
    for i in range(len(times)):
        time += str(times[i])
    distance: str = ''
    for i in range(len(distances)):
        distance += str(distances[i])
    return part1([int(time)], [int(distance)])


def main():
    with open('input/day6.txt') as f:
        times, distances = f.read().splitlines()
    times = [int(x) for x in times.split(': ')[1].strip().split(" ") if x.isdigit()]
    distances = [int(x) for x in distances.split(': ')[1].strip().split(" ") if x.isdigit()]
    print(part1(times, distances))
    print(part2(times, distances))


if __name__ == '__main__':
    main()
