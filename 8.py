import utils
import copy


DAY = 8
TITLE = 'Day 8: Treetop Tree House'


def procress_input(input: list[str]):
    ROWS = len(input)
    COLS = len(input[0])

    visibility = [[False] * COLS for _ in range(ROWS)]
    scenicscore = [[0] * COLS for _ in range(ROWS)]
    for r, _ in enumerate(input):
        for c, height in enumerate(input[r]):
            if r == 0 or r == ROWS - 1 or c == 0 or c == COLS - 1:
                visibility[r][c] = True
                continue

            left = list(input[r][:c])
            left.reverse()
            right = list(input[r][c+1:])
            top = [row[c] for row in input[:r]]
            top.reverse()
            bottom = [row[c] for row in input[r+1:]]

            if height > min(max(left), max(right), max(top), max(bottom)):
                visibility[r][c] = True

            score = 1
            for direction in copy.deepcopy((top, left, right, bottom)):
                count_trees = 0
                while len(direction) > 0:
                    tree_height = direction.pop(0)
                    count_trees += 1
                    if tree_height >= height:
                        break
                score *= count_trees
            scenicscore[r][c] = score

    return visibility, scenicscore


def print_solutions(data: tuple[list[list[bool]], list[list[int]]]):
    utils.print_sol_part(1, sum(row.count(True) for row in data[0]))
    utils.print_sol_part(2, max(max(row) for row in data[1]))


def main():
    utils.print_title(TITLE)
    lines = utils.read_input(DAY)
    data = procress_input(lines)
    print_solutions(data)


if __name__ == '__main__':
    main()
