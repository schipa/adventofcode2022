import utils
from numpy import sign
from functools import cmp_to_key, reduce
from operator import mul


DAY = 13
TITLE = 'Day 13: Distress Signal'

dividers = [[[2]], [[6]]]


def compare(a: int | list, b: int | list) -> int:
    match a, b:
        case int(), int(): return sign(a - b)
        case int(), list(): return compare([a], b)
        case list(), int(): return compare(a, [b])
        case [], []: return 0
        case [], list(): return -1
        case list(), []: return 1
        case _, _: return compare(a[0], b[0]) or compare(a[1:], b[1:])


def procress_input(input: list[str]):
    pairs = [tuple(map(eval, input[idx:idx+2])) for idx in range(0, len(input), 3)]
    comparison = list(map(lambda pair: compare(*pair), pairs))

    packets = [eval(line) for line in input if line != '']
    packets.extend(dividers)
    packets_sorted = sorted(packets, key=cmp_to_key(compare))

    return comparison, packets_sorted


def print_solutions(data: tuple[list[int], list[list]]):
    utils.print_sol_part(1, sum(idx + 1 for idx, sorted in enumerate(data[0]) if sorted < 0))
    utils.print_sol_part(2, reduce(mul, [data[1].index(divider) + 1 for divider in dividers], 1))


def main():
    utils.print_title(TITLE)
    lines = utils.read_input(DAY)
    data = procress_input(lines)
    print_solutions(data)


if __name__ == '__main__':
    main()
