import utils
from numpy import sign
import copy


DAY = 14
TITLE = 'Day 14: Regolith Reservoir'

ROCK = utils.colors.GRAY + '#' + utils.colors.ENDC
AIR  = ' '
SAND = utils.colors.YELLOW + 'O' + utils.colors.ENDC
SAND_START = utils.colors.RED + '+' + utils.colors.ENDC
SAND_START_POS = (500, 0)


def get_min_max(structures: list[list[tuple[int, int]]]):
    minimum = list(SAND_START_POS)
    maximum = list(SAND_START_POS)
    for struct in structures:
        for x, y in struct:
            if x < minimum[0]: minimum[0] = x
            if x > maximum[0]: maximum[0] = x
            if y < minimum[1]: minimum[1] = y
            if y > maximum[1]: maximum[1] = y
    return tuple(minimum), tuple(maximum)


def get_blocks(structures: list[list[tuple[int, int]]]):
    blocks = {}
    for struct in structures:
        for i in range(0, len(struct) - 1):
            fx, fy = struct[i]
            tx, ty = struct[i + 1]
            if fx != tx:
                gaps = range(fx, tx, sign(tx - fx))
                blocks.update([((x, fy), ROCK) for x in gaps])
            else:
                gaps = range(fy, ty, sign(ty - fy))
                blocks.update([((fx, y), ROCK) for y in gaps])
        blocks[struct[-1]] = ROCK
    return blocks


def simulate_sand(part: int, blocks: dict[tuple[int, int], str], minimum: tuple[int, int], maximum: tuple[int, int]):
    blocks = copy.deepcopy(blocks)
    amount_of_sand = 0
    stop = False
    while not stop:
        sand = list(SAND_START_POS)
        while True:
            if sand[1] > maximum[1]:
                if part == 1:
                    stop = True
                else:
                    blocks[tuple(sand)] = SAND
                    amount_of_sand += 1
                break

            # down
            if (sand[0], sand[1] + 1) not in blocks:
                sand[1] += 1
                continue

            # down-left
            if (sand[0] - 1, sand[1] + 1) not in blocks:
                sand[0] -= 1
                sand[1] += 1
                continue

            # down-right
            if (sand[0] + 1, sand[1] + 1) not in blocks:
                sand[0] += 1
                sand[1] += 1
                continue

            # halt
            blocks[tuple(sand)] = SAND
            amount_of_sand += 1

            if part == 2 and tuple(sand) == SAND_START_POS:
                stop = True

            break

    # print_status(blocks, minimum, maximum)
    return amount_of_sand


def print_status(blocks: dict[tuple[int, int], str], minimum: tuple[int, int], maximum: tuple[int, int]):
    x_min, y_min = minimum
    x_max, y_max = maximum
    for y in range(y_min, y_max + 1):
        for x in range(x_min, x_max + 1):
            if (x, y) == SAND_START_POS:
                print(SAND_START, end='')
                continue
            if (x, y) in blocks:
                print(blocks.get((x, y)), end='')
                continue
            print(AIR, end='')
        print()


def procress_input(input: list[str]):
    return [[ tuple(map(int, point.split(','))) for point in line.split(' -> ') ] for line in input]


def main():
    utils.print_title(TITLE)
    lines = utils.read_input(DAY)
    structures = procress_input(lines)
    minimim, maximum = get_min_max(structures)
    blocks = get_blocks(structures)

    for part in (1, 2):
        amount_of_sand = simulate_sand(part, blocks, minimim, maximum)
        utils.print_sol_part(part, amount_of_sand)


if __name__ == '__main__':
    main()
