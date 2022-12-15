import utils


DAY = 9
TITLE = 'Day 9: Rope Bridge'


def move_head(head: tuple[int, int], direction: str):
    hx, hy = head
    match direction:
        case 'U':
            hy += 1
        case 'D':
            hy -= 1
        case 'L':
            hx -= 1
        case 'R':
            hx += 1
    return hx, hy


def tail_follow(tail: tuple[int, int], follow: tuple[int, int]):
    tx, ty = tail
    fx, fy = follow
    dx = abs(fx - tx)
    dy = abs(fy - ty)
    if max(dx, dy) > 1:
        if dx:
            tx += (fx - tx) // dx
        if dy:
            ty += (fy - ty) // dy
    return tx, ty


def print_path(path: list[tuple[int, int]]):
    x_min = min([coord[0] for coord in path])
    x_max = max([coord[0] for coord in path])
    y_min = min([coord[1] for coord in path])
    y_max = max([coord[1] for coord in path])
    origin_x = -x_min
    origin_y = -y_min

    trace = [['.'] * (x_max - x_min + 1) for _ in range(y_max - y_min + 1)]
    for x, y in path:
        trace[origin_y + y][origin_x + x] = '#'
    trace[origin_y][origin_x] = 'S'
    trace.reverse()
    print('\n' + '\n'.join(''.join(row) for row in trace) + '\n')


def procress_input(input: list[str]):
    paths = []
    for length in [2, 10]:
        rope = [(0, 0)] * length
        path = [(0, 0)]
        for line in input:
            direction, steps = line.split(' ')
            for _ in range(int(steps)):
                rope[0] = move_head(rope[0], direction)
                for i in range(1, len(rope)):
                    rope[i] = tail_follow(rope[i], rope[i - 1])
                path.append(rope[-1])
        paths.append(path)
    return paths


def print_solutions(data: list[list[tuple[int, int]]]):
    for part, path in enumerate(data):
        # print_path(path)
        utils.print_sol_part(part + 1, len(set(path)))


def main():
    utils.print_title(TITLE)
    lines = utils.read_input(DAY)
    data = procress_input(lines)
    print_solutions(data)


if __name__ == '__main__':
    main()
