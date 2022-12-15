import utils
from queue import PriorityQueue


DAY = 12
TITLE = 'Day 12: Hill Climbing Algorithm'


def a_star(heightmap: list[list[str]], start: tuple[int, int], end: tuple[int, int]):
    priority_queue = PriorityQueue()
    priority_queue.put((distance(start, end), start))

    came_from = {}
    scores = {start: 0}
    visited = set()

    while priority_queue.qsize() > 0:
        curr: tuple[int, int]
        curr = priority_queue.get()[1]
        visited.add(curr)
        if curr == end:
            continue

        next: tuple[int, int]
        for next in get_next_steps(heightmap, curr):
            score = scores.get(curr) + 1
            if score < scores.get(next, float('inf')):
                came_from[next] = curr
                scores[next] = score
                priority_queue.put((distance(next, end), next))

    return visited, traceback(end, came_from)


def distance(a: tuple[int, int], b: tuple[int, int]):
    return distance_orthogonal(a, b)


def distance_orthogonal(a: tuple[int, int], b: tuple[int, int]):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def distance_euclidean(a: tuple[int, int], b: tuple[int, int]):
    return pow((a[0] - b[0])**2 + (a[1] - b[1])**2, .5)


def get_next_steps(heightmap: list[list[str]], position: tuple[int, int]):
    steps = []
    curr_x, curr_y = position
    curr_height = get_height(heightmap, position)

    neighbors = [
        (curr_x, curr_y - 1),  # up
        (curr_x, curr_y + 1),  # down
        (curr_x - 1, curr_y),  # left
        (curr_x + 1, curr_y)   # right
    ]
    for neighbor in neighbors:
        this_x, this_y = neighbor
        if this_x >= 0 and this_y >= 0 and this_x < len(heightmap[0]) and this_y < len(heightmap):
            this_height = get_height(heightmap, neighbor)
            if this_height <= curr_height + 1:
                steps.append(neighbor)

    return steps


def get_height(heightmap: list[list[str]], position: tuple[int, int]):
    x, y = position
    character = heightmap[y][x]
    if character == 'S':
        return ord('a')
    if character == 'E':
        return ord('z')
    return ord(character)


def traceback(position: tuple[int, int], came_from: dict[tuple[int, int], tuple[int, int]]):
    path = []
    while position in came_from:
        path.append(position)
        position = came_from[position]
    path.append(position)
    return path


def print_heightmap(heightmap: list[list[str]], visited: set[tuple[int, int]], path: list[tuple[int, int]]):
    for row, lst in enumerate(heightmap):
        for col, height in enumerate(lst):
            if (col, row) in path:
                print(utils.colors.BOLD + utils.colors.GREEN + height + utils.colors.ENDC, end='')
            elif (col, row) in visited:
                print(utils.colors.YELLOW + height + utils.colors.ENDC, end='')
            else:
                print(utils.colors.GRAY + height + utils.colors.ENDC, end='')
        print()


def procress_input(input: list[str]):
    start = end = (-1, -1)
    heightmap = []
    for y, line in enumerate(input):
        heightmap.append(list(line))
        if start[0] == -1:
            start = (line.find('S'), y)
        if end[0] == -1:
            end = (line.find('E'), y)
    return heightmap, start, end


def print_solutions(part: int, heightmap: list[list[str]], visited: set[tuple[int, int]], shortest_path: list[tuple[int, int]]):
    print_heightmap(heightmap, visited, shortest_path)
    utils.print_sol_part(part, len(shortest_path) - 1)


def main():
    utils.print_title(TITLE)
    lines = utils.read_input(DAY)
    heightmap, start, end = procress_input(lines)

    # part 1
    visited, shortest_path = a_star(heightmap, start, end)
    print_solutions(1, heightmap, visited, shortest_path)

    # part 2
    shortest_path = None
    for start in [(0, row) for row in range(len(heightmap))]:
        _visited, _shortest_path = a_star(heightmap, start, end)
        if not shortest_path or len(_shortest_path) < len(shortest_path):
            visited = _visited
            shortest_path = _shortest_path
    print_solutions(2, heightmap, visited, shortest_path)


if __name__ == '__main__':
    main()
