class colors:
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    GRAY = '\033[90m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'


def print_title(title: str):
    print(colors.MAGENTA + colors.BOLD + title + colors.ENDC)


def print_sol_part(nr: int, result):
    print('{}Part {}:{} {}'.format(colors.GREEN, nr, colors.ENDC, result))


def read_input(day: int, example: bool = False):
    with open('{}{}-input.txt'.format(day, '-ex' if example else ''), 'r') as f:
        return f.read().splitlines()
