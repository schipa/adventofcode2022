import utils


DAY = 17
TITLE = 'Day 17: Pyroclastic Flow'

# rocks are bottom to top
ROCKS = [
    ['####'],

    [' # ',
     '###',
     ' # '],

    ['###',
     '  #',
     '  #'],

    ['#',
     '#',
     '#',
     '#'],

    ['##',
     '##'],
]
WIDTH = 7
START_COL = 2
START_ROW = 3
TARGET = 10**12


snapshots = {}
def detect_pattern(chamber: list[str], r_iter: int, r_mod: int, j_iter: int, j_mod: int, highest_rock: int):
    if r_iter < 2022:
        return r_iter, 0

    key = (r_iter % r_mod, j_iter % j_mod, ''.join(chamber[max(0, highest_rock + 1 - 10) : highest_rock + 1]))
    if key not in snapshots:
        snapshots[key] = r_iter, highest_rock
        return r_iter, 0

    period_r_iter = r_iter - snapshots[key][0]
    period_height = highest_rock - snapshots[key][1]

    factor = (TARGET - r_iter) // period_r_iter
    r_iter += factor * period_r_iter
    adjustment = factor * period_height

    return r_iter, adjustment


def move_possible(chamber: list[str], rock: list[str], row: int, col: int, direction: str):
    for r in range(len(rock)):
        for c in range(len(rock[r])):
            if rock[r][c] == ' ':
                continue

            match direction:
                case 'left':
                    if col == 0 or chamber[row + r][col + c - 1] != ' ':
                        return False

                case 'right':
                    if col + len(rock[0]) == len(chamber[0]) or chamber[row + r][col + c + 1] != ' ':
                        return False

                case 'down':
                    if row == 1 or chamber[row - 1 + r][col + c] != ' ':
                        return False

    return True


def land_rock(chamber: list[str], rock: list[str], row: int, col: int):
    for r in range(len(rock)):
        for c in range(len(rock[r])):
            if rock[r][c] == ' ':
                continue
            chamber[row + r] = chamber[row + r][:col + c] + rock[r][c] + chamber[row + r][col + c + 1:]

    highest_rock = 0
    for ch, cr in reversed(list(enumerate(chamber))):
        if cr.count('#') > 0:
            highest_rock = ch
            break
    return highest_rock


def main():
    utils.print_title(TITLE)
    [jet_pattern] = utils.read_input(DAY)

    chamber = ['–' * WIDTH]

    j = 0
    r = 0
    highest_rock = 0
    adjustment = 0
    while r < TARGET:
        # get next shape
        rock = ROCKS[r % len(ROCKS)]
        r += 1

        # extend chamber if needed
        chamber.extend([' ' * WIDTH for _ in range(max(0, highest_rock + START_ROW + len(rock) - len(chamber) + 1))])

        # starting position
        col = START_COL
        row = highest_rock + START_ROW + 1

        while True:
            # get next jet
            jet = jet_pattern[j % len(jet_pattern)]
            j += 1

            # push from jet
            match jet:
                case '<':
                    if move_possible(chamber, rock, row, col, 'left'):
                        col -= 1
                case '>':
                    if move_possible(chamber, rock, row, col, 'right'):
                        col += 1

            # falling
            if move_possible(chamber, rock, row, col, 'down'):
                row -= 1
                continue

            # landing
            highest_rock = land_rock(chamber, rock, row, col)
            break

        if adjustment == 0:
            r, adjustment = detect_pattern(chamber, r, len(ROCKS), j, len(jet_pattern), highest_rock)

        if r == 2022:
            utils.print_sol_part(1, highest_rock + adjustment)

    utils.print_sol_part(2, highest_rock + adjustment)


if __name__ == '__main__':
    main()
