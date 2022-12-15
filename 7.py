import utils


DAY = 7
TITLE = 'Day 7: No Space Left On Device'

SMALL_LIMIT  = 100000
SPACE_TOTAL  = 70000000
SPACE_NEEDED = 30000000


def procress_input(input: list[str]):
    cwd = []
    filesystem = {}
    for line in input:
        # handle `$ cd DIR`
        if line.startswith('$ cd '):
            directory = line[5:]
            if directory == '..':
                cwd.pop()
            else:
                cwd.append(directory)
            continue

        absolute_path = '/' + '/'.join(cwd[1:])

        # handle `$ ls`
        if line == '$ ls':
            filesystem[absolute_path] = {}
            continue

        # handle `dir DIR_NAME` (ignore)
        if line.startswith('dir '):
            continue

        # handle `SIZE FILE_NAME`
        size, file_name = line.split(' ')
        filesystem[absolute_path][file_name] = int(size)

    return filesystem


def print_solutions(filesystem: dict):
    directory_sizes = {}

    path: str
    files: dict
    for path, files in filesystem.items():
        size = sum(files.values())
        directory_sizes[path] = size

        # add size to parent directory, up to root
        while path != '/':
            path = path[:path.rfind('/')] if path.count('/') > 1 else '/'
            directory_sizes[path] += size

    utils.print_sol_part(1, sum(size for size in directory_sizes.values() if size <= SMALL_LIMIT))
    SPACE_FREE = SPACE_TOTAL - directory_sizes['/']
    utils.print_sol_part(2, min(size for size in directory_sizes.values() if size >= SPACE_NEEDED - SPACE_FREE))


def main():
    utils.print_title(TITLE)
    lines = utils.read_input(DAY)
    data = procress_input(lines)
    print_solutions(data)


if __name__ == '__main__':
    main()
