import utils
import re


DAY = 21
TITLE = 'Day 21: Monkey Math'


def calc(monkeys: dict[str, str], name: str, only_substitute: bool = False):
    formula = monkeys[name]

    if only_substitute:
        if name == 'root':
            formula = formula.replace(formula[5], '=')
        elif name == 'humn':
            return name

    if re.match(r'\d+', formula):
        return int(formula)

    for other in re.findall(r'\w+', formula):
        value = calc(monkeys, other, only_substitute)
        formula = formula.replace(other, str(value))

    if only_substitute and formula.find('humn') != -1:
        return '({})'.format(formula)

    return int(eval(formula))


def simple_solver(formula: str, value: int = -1) -> int:
    match = re.match(r'^\(([^\(\)]+) (.) (.+)\)$', formula)
    if not match:
        match = re.match(r'^\((.+) (.) ([^\(\)]+)\)$', formula)
    assert match is not None
    lh, op, rh = match.groups()

    humn_is_left_hand = True if lh.find('humn') != -1 else False

    formula = lh if humn_is_left_hand else rh
    match op:
        case '=':
            value = int(rh) if humn_is_left_hand else int(lh)

        case '+':
            value -= int(rh) if humn_is_left_hand else int(lh)

        case '-':
            if humn_is_left_hand:
                value += int(rh)
            else:
                value -= int(lh)
                value *= -1

        case '*':
            value //= int(rh) if humn_is_left_hand else int(lh)

        case '/':
            if humn_is_left_hand:
                value *= int(rh)
            else:
                value = 1 // value
                value *= int(rh)

    if formula == 'humn':
        return value

    return simple_solver(formula, value)


def procress_input(input: list[str]):
    monkeys = {}
    for line in input:
        match = re.match(r'(\w+): (.+)', line)
        assert match is not None
        name, formula = match.groups()
        monkeys[name] = formula
    return monkeys


def main():
    utils.print_title(TITLE)
    lines = utils.read_input(DAY, example=False)
    monkeys = procress_input(lines)

    utils.print_sol_part(1, calc(monkeys, name='root'))

    equation = calc(monkeys, name='root', only_substitute=True)
    assert isinstance(equation, str)
    utils.print_sol_part(2, simple_solver(equation))


if __name__ == '__main__':
    main()
