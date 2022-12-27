import utils
from copy import deepcopy


DAY = 20
TITLE = 'Day 20: Grove Positioning System'


def mix(data: list[list[int]], repetitions: int = 1):
    zero = -1
    for _ in range(repetitions):
        for this, (prv, value, nxt) in enumerate(data):
            if value == 0:
                zero = this
                continue

            data[prv][2] = nxt
            data[nxt][0] = prv

            for _ in range(value % (len(data) - 1)):
                nxt = data[nxt][2]
            data[this][2] = nxt
            prv = data[nxt][0]
            data[this][0] = prv

            data[prv][2] = this
            data[nxt][0] = this

    return zero


def procress_input(input: list[str]):
    # double linked list with pointers to prev and next index
    return [[(l - 1) % len(input), int(line), (l + 1) % len(input)] for l, line in enumerate(input)]


def main():
    utils.print_title(TITLE)
    lines = utils.read_input(DAY)
    data = procress_input(lines)

    for part, repetitions, multiplier in [(1, 1, 1), (2, 10, 811589153)]:
        data_part = [[p, v * multiplier, n] for p, v, n in deepcopy(data)]
        zero = mix(data_part, repetitions)

        data_sorted = [data_part[zero]]
        while len(data_part) != len(data_sorted):
            data_sorted.append(data_part[data_sorted[-1][2]])

        numbers_sorted = [v for _, v, _ in data_sorted]
        utils.print_sol_part(part, sum([numbers_sorted[nri % len(numbers_sorted)] for nri in [1000, 2000, 3000]]))


if __name__ == '__main__':
    main()
