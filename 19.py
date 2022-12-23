import utils
import re
import numpy as np
from functools import reduce
from operator import mul


DAY = 19
TITLE = 'Day 19: Not Enough Minerals'


best = 0
def open_geodes(blueprint: tuple[int, list[list[int]]], time: int):
    global best
    best = 0

    id, costs = blueprint
    max_costs: list[int] = np.amax(costs, axis=0)
    robots = [1, 0, 0, 0]
    resources = [0, 0, 0, 0]

    print('Blueprint {} '.format(id), end='', flush=True)
    run(costs, max_costs, robots, resources, time)
    print('can open {} geodes in {} minutes.'.format(best, time))

    return id, best


def run(costs: list[list[int]], max_costs: list[int], robots_start: list[int], resources_start: list[int], minutes_left: int):
    global best

    idle = resources_start[3] + robots_start[3] * minutes_left
    if idle > best:
        best = idle
    opti = idle + (minutes_left * (minutes_left - 1) // 2)
    if opti <= best:
        return

    for index, cost in reversed(list(enumerate(costs))):
        if index < 3 and robots_start[index] >= max_costs[index]:
            continue
        wait = waiting_time(tuple(cost), tuple(resources_start), tuple(robots_start))
        if wait != None and wait < minutes_left:
            robots = robots_start.copy()
            robots[index] += 1
            resources = list(resources_start + np.array(robots_start) * (wait + 1) - cost)
            run(costs, max_costs, robots, resources, minutes_left - wait - 1)


def waiting_time(cost: tuple[int], resources: tuple[int], robots: tuple[int]):
    time: list[int] = []
    for c, r, b in zip(cost, resources, robots):
        if r >= c:
            time.append(0)
        elif b:
            time.append((c - r + b - 1) // b)
        else:
            return None
    return max(time) if time else None


def procress_input(input: list[str]):
    blueprints = []
    for blueprint in input:
        ints = list(map(int, re.findall('\\d+', blueprint)))
        blueprints.append((
            ints[0],
            [
                [ints[1],       0,       0,       0],
                [ints[2],       0,       0,       0],
                [ints[3], ints[4],       0,       0],
                [ints[5],       0, ints[6],       0],
            ],
        ))
    return blueprints


def main():
    utils.print_title(TITLE)
    lines = utils.read_input(DAY)
    blueprints = procress_input(lines)

    utils.print_sol_part(1, sum([id * geodes for id, geodes in [open_geodes(bp, 24) for bp in blueprints]]))
    utils.print_sol_part(2, reduce(mul, [open_geodes(bp, 32)[1] for bp in blueprints[:3]], 1))


if __name__ == '__main__':
    main()
