import utils


DAY = 10
TITLE = 'Day 10: Cathode-Ray Tube'

cycle = 0
register = {'X': 1}
readout = []
crt = [[' '] * 40 for _ in range(6)]
sprite = '###'


def tick():
    global cycle
    cycle += 1

    # part 1
    if cycle % 40 == 20:
        signal_strength = cycle * register['X']
        readout.append(signal_strength)

    # part 2
    row = (cycle - 1) // 40
    col = (cycle - 1) % 40
    sprite_pixel = col - (register['X'] - 1)
    if sprite_pixel in range(0, len(sprite)):
        crt[row][col] = sprite[sprite_pixel]


def procress_input(input: list[str]):
    for line in input:
        instruction = line[0:4]
        match instruction:
            case 'noop':
                tick()
            case 'addx':
                tick()
                tick()
                register['X'] += int(line[5:])


def print_solutions():
    utils.print_sol_part(1, sum(readout))
    display = '\n'.join(''.join(cell for cell in row) for row in crt)
    utils.print_sol_part(2, 'CRT:\n' + display)


def main():
    utils.print_title(TITLE)
    lines = utils.read_input(DAY)
    procress_input(lines)
    print_solutions()


if __name__ == '__main__':
    main()
