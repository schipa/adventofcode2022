import utils
import numpy as np


DAY = 18
TITLE = 'Day 18: Boiling Boulders'

DIRECTIONS = [
    (-1, 0, 0),
    ( 1, 0, 0),
    ( 0,-1, 0),
    ( 0, 1, 0),
    ( 0, 0,-1),
    ( 0, 0, 1),
]


def get_min_max(cubes: list[tuple[int, int, int]]):
    min_max = [(float('inf'), float('-inf')) for _ in range(3)]
    for cube in cubes:
        min_max[0] = min(min_max[0][0], cube[0]), max(min_max[0][1], cube[0])
        min_max[1] = min(min_max[1][0], cube[1]), max(min_max[1][1], cube[1])
        min_max[2] = min(min_max[2][0], cube[2]), max(min_max[2][1], cube[2])
    return min_max


air_inside = []
air_outside = []
def side_is_exterior(cubes: list[tuple[int, int, int]], min_max: list[tuple[int, int, int]], air: tuple[int, int, int]):
    test = set([air])
    checked = []
    while len(test) > 0:
        spot = test.pop()
        if spot in cubes or spot in checked:
            continue
        if spot in air_inside:
            air_inside.extend(checked)
            return False
        if spot in air_outside or any([not min_max[a][0] <= v <= min_max[a][1] for a, v in enumerate(spot)]):
            air_outside.extend(checked)
            return True

        checked.append(spot)
        for dir in DIRECTIONS:
            test.add(tuple(np.array(spot) + dir))

    air_inside.extend(checked)
    return False


def procress_input(input: list[str]):
    return [tuple(map(int, line.split(','))) for line in input]


def main():
    utils.print_title(TITLE)
    lines = utils.read_input(DAY)
    cubes = procress_input(lines)
    min_max = get_min_max(cubes)

    surface_area = 0
    surface_area_ex = 0
    for cube in cubes:
        for dir in DIRECTIONS:
            side = tuple(np.array(cube) + dir)
            if side not in cubes:
                surface_area += 1
                if side_is_exterior(cubes, min_max, side):
                    surface_area_ex += 1

    utils.print_sol_part(1, surface_area)
    utils.print_sol_part(2, surface_area_ex)


if __name__ == '__main__':
    main()
