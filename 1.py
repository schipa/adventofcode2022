import utils


DAY = 1
TITLE = 'Day 1: Calorie Counting'


def procress_input(input: list[str]):
    data = []
    i = 0
    for line in input:
        if line == '':
            i += 1
            continue
        if len(data) == i:
            data.append(0)
        data[i] += int(line)
    return data


def print_solutions(data: list[int]):
    utils.print_sol_part(1, max(data))

    data.sort()
    utils.print_sol_part(2, sum(data[-3:]))


def main():
    utils.print_title(TITLE)
    lines = utils.read_input(DAY)
    data = procress_input(lines)
    print_solutions(data)


if __name__ == '__main__':
    main()
