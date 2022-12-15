import utils


DAY = 3
TITLE = 'Day 3: Rucksack Reorganization'


def check_rucksack(items: str):
    mid = len(items) // 2
    compartment1 = items[:mid]
    compartment2 = items[mid:]
    return ''.join(set(compartment1).intersection(compartment2))


def check_group(group: list[str]):
    badge = set(group[0])
    for i in range(1, len(group)):
        badge = badge.intersection(group[i])
    return ''.join(badge)


def item_priority(item: str):
    if item.islower():
        return ord(item) - 97 + 1
    return ord(item) - 65 + 27


def procress_input(input: list[str]):
    grouped_input = [input[i:i+3] for i in range(0, len(input), 3)]
    return (
        list(map(check_rucksack, input)),
        list(map(check_group, grouped_input))
    )


def print_solutions(data: tuple[list[str], list[str]]):
    utils.print_sol_part(1, sum(map(item_priority, data[0])))
    utils.print_sol_part(2, sum(map(item_priority, data[1])))


def main():
    utils.print_title(TITLE)
    lines = utils.read_input(DAY)
    data = procress_input(lines)
    print_solutions(data)


if __name__ == '__main__':
    main()
