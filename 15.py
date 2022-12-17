import utils
import re


DAY = 15
TITLE = 'Day 15: Beacon Exclusion Zone'


def distance(a: tuple[int, int], b: tuple[int, int]):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def get_cover_for_row(data: list[tuple[int, int, int, int]], row: int):
    intervals = []
    beacons = []
    for xs, ys, xb, yb in data:
        distance_beacon = distance((xs, ys), (xb, yb))
        distance_row = abs(ys - row)
        if distance_row <= distance_beacon:
            span = distance_beacon - distance_row
            intervals.append((xs - span, xs + span))
            if yb == row and xb not in beacons:
                beacons.append(xb)

    intervals.sort()
    covered = []
    for lo, hi in intervals:
        if not covered or lo > covered[-1][1] + 1:
            covered.append([lo, hi])
            continue

        covered[-1][1] = max(covered[-1][1], hi)

    return covered, beacons


def get_boundary(sensor: tuple[int, int, int, int], xy_min: int, xy_max: int):
    boundary = set()
    xs, ys, xb, yb = sensor
    distance_boundary = distance((xs, ys), (xb, yb)) + 1
    for y in range(ys - distance_boundary, ys + distance_boundary + 1):
        if y < xy_min: continue
        if y > xy_max: break
        x_plus_minus = distance_boundary - abs(ys - y)
        for x in (xs - x_plus_minus, xs + x_plus_minus):
            if x < xy_min: continue
            if x > xy_max: break
            boundary.add((x, y))
    return boundary


def procress_input(input: list[str]):
    sensor_data = []
    pattern = re.compile(r'-?\d+')
    for line in input:
        sensor_data.append(tuple(map(int, pattern.findall(line))))
    return sensor_data


def print_solutions(data: list[tuple[int, int, int, int]]):
    row = 2000000
    covered, beacons = get_cover_for_row(data, row)
    utils.print_sol_part(1, sum([hi - lo + 1 for lo, hi in covered]) - len(beacons))

    for y in range(row * 2 + 1):
        covered, _ = get_cover_for_row(data, y)
        if len(covered) == 1:
            continue
        x = covered[0][1] + 1
        utils.print_sol_part(2, '{} = {}'.format((x, y), x * 4000000 + y))
        break


def main():
    utils.print_title(TITLE)
    lines = utils.read_input(DAY)
    data = procress_input(lines)
    print_solutions(data)


if __name__ == '__main__':
    main()
