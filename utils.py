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
    print(colors.GREEN + ('Part %d: ' % nr) + colors.ENDC + ('%s' % result))


def read_input(day: int):
    with open('%d-input.txt' % day, 'r') as f:
        return f.read().splitlines()
