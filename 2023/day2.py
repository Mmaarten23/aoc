class Game:
    def __init__(self, game_id: int, showings: list[dict[str, int]]) -> None:
        self.id = game_id
        self.showings = showings

    def __repr__(self) -> str:
        return f'Game {self.id}, {self.showings}'

    def __str__(self) -> str:
        return f'Game {self.id}, {self.showings}'


def part1(games: list[Game]) -> int:
    maximum: dict[str, int] = {"red": 12, "green": 13, "blue": 14}
    valid = []
    for game in games:
        is_valid: bool = True
        for showing in game.showings:
            for color, amount in showing.items():
                if amount > maximum[color]:
                    is_valid = False
                    break
        if is_valid:
            valid.append(game)
    return sum([game.id for game in valid])


def part2(games: list[Game]) -> int:
    s: int = 0
    for game in games:
        current_max: dict[str, int] = {"red": 0, "green": 0, "blue": 0}
        for showing in game.showings:
            for color, amount in showing.items():
                if amount > current_max[color]:
                    current_max[color] = amount
        s += current_max["red"] * current_max["green"] * current_max["blue"]
    return s


def main():
    with open('input/day2.txt', 'r') as file:
        lines: list[str] = file.readlines()
    # Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
    games: list[Game] = []
    for line in lines:
        game_identification, showings_str = line.split(':')
        game_id: int = int(game_identification.split(' ')[1])
        showings: list[dict[str, int]] = []
        for showing in showings_str.split(';'):
            showing_dict: dict[str, int] = {}
            for color_amount in showing.split(','):
                amount, color = color_amount.strip().split(' ')
                showing_dict[color.strip()] = int(amount.strip())
            showings.append(showing_dict)
        games.append(Game(game_id, showings))
    part1(games)
    part2(games)


if __name__ == '__main__':
    main()
