import utils


DAY = 6
TITLE = 'Day 6: Tuning Trouble'

PACKET_MARKER_LENGTH = 4
MESSAGE_MARKER_LENGTH = 14


def procress_input(input: str):
    l = 0
    r = PACKET_MARKER_LENGTH
    while len(set(input[l:r])) != PACKET_MARKER_LENGTH:
        l += 1
        r += 1
    start_of_packet = r
    r = l + MESSAGE_MARKER_LENGTH
    while len(set(input[l:r])) != MESSAGE_MARKER_LENGTH:
        l += 1
        r += 1
    start_of_message = r
    return start_of_packet, start_of_message


def print_solutions(data: tuple[int, int]):
    utils.print_sol_part(1, data[0])
    utils.print_sol_part(2, data[1])


def main():
    utils.print_title(TITLE)
    [line] = utils.read_input(DAY)
    data = procress_input(line)
    print_solutions(data)


if __name__ == '__main__':
    main()
