import utils


DAY = 4
TITLE = 'Day 4: Camp Cleanup'


def pair_to_set_of_sections(pair: str):
    a, b = pair.split(',')
    a_start, a_end = map(int, a.split('-'))
    b_start, b_end = map(int, b.split('-'))
    a_sections = set(range(a_start, a_end + 1))
    b_sections = set(range(b_start, b_end + 1))
    return (a_sections, b_sections)


def procress_input(input: list[str]):
    data = list(map(pair_to_set_of_sections, input))
    count_full_overlap = 0
    count_overlap = 0
    for a_sections, b_sections in data:
        if max(len(a_sections), len(b_sections)) == len(a_sections.union(b_sections)):
            count_full_overlap += 1
        if a_sections.intersection(b_sections):
            count_overlap += 1
    return count_full_overlap, count_overlap


def print_solutions(data: tuple[int]):
    utils.print_sol_part(1, data[0])
    utils.print_sol_part(2, data[1])


def main():
    utils.print_title(TITLE)
    lines = utils.read_input(DAY)
    data = procress_input(lines)
    print_solutions(data)


if __name__ == '__main__':
    main()
