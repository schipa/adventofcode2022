import utils
from functools import reduce
from operator import mul


DAY = 11
TITLE = 'Day 11: Monkey in the Middle'


class Monkey:
    _items_init: list[int]
    _items: list[int]
    _operation: str
    _test: int
    _on_true: int
    _on_false: int
    _count_inspections: int

    def __init__(self, items: list[int], operation: str, test: int, on_true: int, on_false: int):
        self._items_init = items.copy()
        self._operation = operation
        self._test = test
        self._on_true = on_true
        self._on_false = on_false
        self.reset()

    def get_test(self):
        return self._test

    def inspect_item(self, relief: int | None, mod: int | None):
        if len(self._items) == 0:
            return None

        item = self._items.pop(0)
        ldict = {'old': item}
        exec(self._operation, globals(), ldict)
        if relief:
            item = ldict['new'] // relief
        elif mod:
            item = ldict['new'] % mod
        new_monkey = self._on_true if item % self._test == 0 else self._on_false

        self._count_inspections += 1
        return (item, new_monkey)

    def add_item(self, item: int):
        self._items.append(item)

    def count_inspections(self):
        return self._count_inspections

    def reset(self):
        self._items = self._items_init.copy()
        self._count_inspections = 0


def procress_input(input: list[str]) -> list[Monkey]:
    monkeys = []
    descriptions = [line for line in input if line != '']
    for index, items, operation, test, true, false in zip(*[iter(descriptions)]*6):
        index = int(index[7:-1])
        items = list(map(int, str(items[18:]).split(', ')))
        operation = str(operation[13:])
        test = int(test[21:])
        true = int(true[29:])
        false = int(false[30:])
        monkeys.append(Monkey(items, operation, test, true, false))
    return monkeys


def print_solutions(monkeys: list[Monkey]):
    for part, rounds, relief in [(1, 20, 3), (2, 10000, None)]:
        modulo = None
        if relief == None:
            modulo = reduce(mul, [monkey.get_test() for monkey in monkeys], 1)

        for monkey in monkeys:
            monkey.reset()

        count_inspections = process_rounds(monkeys, rounds, relief, modulo)
        count_inspections.sort(reverse=True)
        utils.print_sol_part(part, count_inspections[0] * count_inspections[1])


def process_rounds(monkeys: list[Monkey], rounds: int, relief: int | None, modulo: int | None):
    for _ in range(rounds):
        for monkey in monkeys:
            while True:
                result = monkey.inspect_item(relief, modulo)
                if result == None:
                    break
                item, index = result
                monkeys[index].add_item(item)

    return [monkey.count_inspections() for monkey in monkeys]


def main():
    utils.print_title(TITLE)
    lines = utils.read_input(DAY)
    data = procress_input(lines)
    print_solutions(data)


if __name__ == '__main__':
    main()
