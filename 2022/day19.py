import re
from re import Match


class Blueprint:
    def __init__(self, blueprint_id: int, ore_cost: int, clay_cost: int, obsidian_ore_cost: int,
                 obsidian_clay_cost: int, geode_ore_cost: int, geode_obsidian_cost: int):
        self.blueprint_id: int = blueprint_id
        self.ore_cost: int = ore_cost
        self.clay_cost: int = clay_cost
        self.obsidian_ore_cost: int = obsidian_ore_cost
        self.obsidian_clay_cost: int = obsidian_clay_cost
        self.geode_ore_cost: int = geode_ore_cost
        self.geode_obsidian_cost: int = geode_obsidian_cost

    def __repr__(self) -> str:
        return f'Blueprint({self.blueprint_id}, {self.ore_cost}, {self.clay_cost}, {self.obsidian_ore_cost}, {self.obsidian_clay_cost}, {self.geode_ore_cost}, {self.geode_obsidian_cost})'


class State:
    def __init__(self,
                 ore: int = 0,
                 clay: int = 0,
                 obsidian: int = 0,
                 geodes: int = 0,
                 ore_robots: int = 0,
                 clay_robots: int = 0,
                 obsidian_robots: int = 0,
                 geode_robots: int = 0,
                 building: str = None):
        self.ore: int = ore
        self.clay: int = clay
        self.obsidian: int = obsidian
        self.geodes: int = geodes
        self.ore_robots: int = ore_robots
        self.clay_robots: int = clay_robots
        self.obsidian_robots: int = obsidian_robots
        self.geode_robots: int = geode_robots
        self.building: str = building

    def __str__(self):
        return f'Ore: {self.ore}, Clay: {self.clay}, Obsidian: {self.obsidian}, Geodes: {self.geodes}, Ore Robots: {self.ore_robots}, Clay Robots: {self.clay_robots}, Obsidian Robots: {self.obsidian_robots}, Geode Robots: {self.geode_robots}, Building: {self.building}'

    def clone(self):
        return State(self.ore, self.clay, self.obsidian, self.geodes, self.ore_robots, self.clay_robots,
                     self.obsidian_robots, self.geode_robots)

    def __eq__(self, other):
        if isinstance(other, State):
            return self.ore == other.ore and \
                self.clay == other.clay and \
                self.obsidian == other.obsidian and \
                self.geodes == other.geodes and \
                self.ore_robots == other.ore_robots and \
                self.clay_robots == other.clay_robots and \
                self.obsidian_robots == other.obsidian_robots and \
                self.geode_robots == other.geode_robots and \
                self.building == other.building
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.__repr__())


def main():
    lines: list[str] = open("test_data.txt").readlines()
    blueprints: list[Blueprint] = parse(lines)
    results_1: list[int] = []
    for blueprint in blueprints:
        results_1.append(run_simulation(blueprint))
    print(results_1)


def parse(lines: list[str]) -> list[Blueprint]:
    blueprints: list[Blueprint] = []
    for line in lines:
        match: Match = re.match(r'Blueprint (\d+): '
                                r'Each ore robot costs (\d+) ore\. '
                                r'Each clay robot costs (\d+) ore\. '
                                r'Each obsidian robot costs (\d+) ore and (\d+) clay\. '
                                r'Each geode robot costs (\d+) ore and (\d+) obsidian\.', line)
        if match is None:
            raise ValueError(f'Invalid line: {line}')
        blueprint: Blueprint = Blueprint(int(match.group(1)), int(match.group(2)), int(match.group(3)),
                                         int(match.group(4)), int(match.group(5)), int(match.group(6)),
                                         int(match.group(7)))
        blueprints.append(blueprint)

    return blueprints


def run_simulation(blueprint: Blueprint) -> int:
    state: State = State(ore_robots=1)
    return step({state}, blueprint, 24)


def step(states: set[State], blueprint: Blueprint, time: int) -> int:
    print(time)
    if time == 0:
        return max(states, key=lambda s: s.geodes).geodes
    new_states: set[State] = set()
    for state in states:
        for building in can_build(state, blueprint):
            new_state: State = state.clone()
            new_state.building = building
            start_build(new_state, blueprint)
            gather_resources(new_state)
            finish_build(new_state)
            new_states.add(new_state)
    return step(new_states, blueprint, time - 1)


def filter_states(new_states: set[State]) -> set[State]:
    to_remove = set()
    for state_1 in new_states:
        for state_2 in new_states:
            if state_1 == state_2:
                continue
            if state_1.ore >= state_2.ore and \
                    state_1.clay >= state_2.clay and \
                    state_1.obsidian >= state_2.obsidian and \
                    state_1.geodes >= state_2.geodes and \
                    state_1.ore_robots <= state_2.ore_robots and \
                    state_1.clay_robots <= state_2.clay_robots and \
                    state_1.obsidian_robots <= state_2.obsidian_robots and \
                    state_1.geode_robots <= state_2.geode_robots:
                to_remove.add(state_2)
    for state in to_remove:
        new_states.remove(state)
    return new_states


def start_build(state: State, blueprint: Blueprint) -> None:
    if state.building == 'ore':
        state.ore -= blueprint.ore_cost
    elif state.building == 'clay':
        state.ore -= blueprint.clay_cost
    elif state.building == 'obsidian':
        state.ore -= blueprint.obsidian_ore_cost
        state.clay -= blueprint.obsidian_clay_cost
    elif state.building == 'geode':
        state.ore -= blueprint.geode_ore_cost
        state.obsidian -= blueprint.geode_obsidian_cost


def gather_resources(state: State) -> None:
    state.ore += state.ore_robots
    state.clay += state.clay_robots
    state.obsidian += state.obsidian_robots
    state.geodes += state.geode_robots


def finish_build(state: State) -> None:
    if state.building == 'ore':
        state.ore_robots += 1
    elif state.building == 'clay':
        state.clay_robots += 1
    elif state.building == 'obsidian':
        state.obsidian_robots += 1
    elif state.building == 'geode':
        state.geode_robots += 1


def can_build(state: State, blueprint: Blueprint) -> list[str]:
    build: list[str] = [None]
    if state.ore >= blueprint.geode_ore_cost and state.obsidian >= blueprint.geode_obsidian_cost:
        build.append('geode')
    if state.ore >= blueprint.obsidian_ore_cost and state.clay >= blueprint.obsidian_clay_cost:
        build.append('obsidian')
    if state.ore >= blueprint.clay_cost:
        build.append('clay')
    # if state.ore >= blueprint.ore_cost:
    #    build.append('ore')
    return build


if __name__ == '__main__':
    main()
