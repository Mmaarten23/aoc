opponent_choices: list[str] = ["A", "B", "C"]
me_choices: list[str] = ["X", "Y", "Z"]


def main():
    text: list[str] = open('input/input2.txt', 'r').read().split("\n")
    score_1: int = 0
    score_2: int = 0
    for line in text:
        (opponent, me) = line.split(" ")
        score_1 += get_score(me)
        score_1 += get_result(opponent, me)

        my_play = get_play(opponent, me)
        score_2 += get_score(my_play)
        score_2 += get_result(opponent, my_play)
    print(f'Part 1: {score_1}')
    print(f'Part 2: {score_2}')


def get_score(me: str) -> int:
    return {"X": 1, "Y": 2, "Z": 3}[me]


def get_result(opponent: str, me: str) -> int:
    if opponent_choices.index(opponent) == (me_choices.index(me) - 1) % 3:
        return 6
    if opponent_choices.index(opponent) == (me_choices.index(me) + 1) % 3:
        return 0
    return 3


def get_play(opponent: str, me: str) -> str:
    if me == "Z":
        return me_choices[(opponent_choices.index(opponent) + 1) % 3]
    if me == "X":
        return me_choices[(opponent_choices.index(opponent) - 1) % 3]
    return me_choices[opponent_choices.index(opponent)]


if __name__ == '__main__':
    main()
