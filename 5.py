import utils
import re
import copy


DAY = 5
TITLE = 'Day 5: Supply Stacks'


def rearrange_9000(stacks: list[list[str]], moves: list[tuple[int, int, int]]):
    stacks = copy.deepcopy(stacks)
    for qty, frm, to in moves:
        while qty > 0:
            stacks[to - 1].append(stacks[frm - 1].pop())
            qty -= 1
    return stacks


def rearrange_9001(stacks: list[list[str]], moves: list[tuple[int, int, int]]):
    stacks = copy.deepcopy(stacks)
    for qty, frm, to in moves:
        stacks[to - 1].extend(stacks[frm - 1][-qty:])
        stacks[frm - 1] = stacks[frm - 1][:-qty]
    return stacks


def get_list_of_moves(input: list[str]):
    return list(map(lambda move: tuple(map(int, re.match('move (\d+) from (\d+) to (\d+)', move).groups())), input))


def procress_input(input: list[str]):
    nr_of_stacks = (len(input[0]) + 1) // 4
    stacks = [[] for _ in range(nr_of_stacks)]
    while input[0][0] != ' ':
        line = input.pop(0)
        s = 0
        while line:
            crate = line[1:2]
            if crate != ' ':
                stacks[s].insert(0, crate)
            line = line[4:]
            s += 1
    moves = get_list_of_moves(input[2:])
    return stacks, moves


def print_solutions(stacks: list[list[str]], moves: list[tuple[int, int, int]]):
    stacks_9000 = rearrange_9000(stacks, moves)
    top_crates_9000 = ''.join(map(lambda stack: stack[-1], stacks_9000))
    utils.print_sol_part(1, top_crates_9000)

    stacks_9001 = rearrange_9001(stacks, moves)
    top_crates_9001 = ''.join(map(lambda stack: stack[-1], stacks_9001))
    utils.print_sol_part(2, top_crates_9001)


def main():
    utils.print_title(TITLE)
    lines = utils.read_input(DAY)
    stacks, moves = procress_input(lines)
    print_solutions(stacks, moves)


if __name__ == '__main__':
    main()
