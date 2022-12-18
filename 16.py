import utils
import re
from more_itertools import powerset


DAY = 16
TITLE = 'Day 16: Proboscidea Volcanium'


def floyd_warshall_dist(valves: dict[str, tuple[int, list[str]]]):
    l = len(valves)
    dist = [[float('inf')] * l for _ in range(l)]
    for v, valve in enumerate(valves.keys()):
        dist[v][v] = 0
        for tunnel in valves[valve][1]:
            w = list(valves.keys()).index(tunnel)
            dist[v][w] = 1
    for k in range(l):
        for i in range(l):
            for j in range(l):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist


def dfs(
    valves: dict[str, tuple[int, list[str]]],
    dist: list[list[int]],
    pos: int,
    closed: list[str],
    time: int
) -> int:
    if not closed:
        return 0
    scores = [0]
    for i, valve in enumerate(closed):
        idx = list(valves.keys()).index(valve)
        time_left = time - dist[pos][idx] - 1
        if time_left > 0:
            s = len(scores)
            scores.append(time_left * valves[valve][0])
            scores[s] += dfs(valves, dist, idx, closed[:i] + closed[i+1:], time_left)
    return max(scores)


def procress_input(input: list[str]):
    valves = {}
    for line in input:
        name, flow_rate, tunnels = re.match('Valve (.+) has flow rate=(\d+); tunnels? leads? to valves? (.+)', line).groups()
        valves[name] = (int(flow_rate), tunnels.split(', '))
    return valves


def main():
    utils.print_title(TITLE)
    lines = utils.read_input(DAY)
    valves = procress_input(lines)
    dist = floyd_warshall_dist(valves)

    aa_index = list(valves.keys()).index('AA')
    closed = [valve[0] for valve in valves.items() if valve[1][0] > 0]

    score = dfs(valves, dist, aa_index, closed, 30)
    utils.print_sol_part(1, score)

    powset = list(powerset(closed))
    total = len(powset) // 2
    score = 0
    for i in range(total):
        print('\r\033[K{}/{} ({:.2f} %) max: {} '.format(i + 1, total, 100 * (i+1) / total, score), end='')
        score = max(
            score,
            dfs(valves, dist, aa_index, powset[i], 26) +
            dfs(valves, dist, aa_index, powset[-i - 1], 26)
        )
    print('\r\033[K', end='')
    utils.print_sol_part(2, score)


if __name__ == '__main__':
    main()
