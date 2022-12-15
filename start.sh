#!/usr/bin/env bash
cd "$(dirname "$0")"

if [ $# -ne 1 ]; then
    echo "Missing DAY argument."
    exit 1
fi

DAY=$1

if [ ! -f "session" ]; then
    echo "File \"$(dirname "$0")/session\" (HTTP Cookie File) not found."
    exit 1
fi

INPUT_FILE_URL="https://adventofcode.com/2022/day/$DAY/input"
INPUT_FILE_PATH="$DAY-input.txt"
if [ ! -f "$INPUT_FILE_PATH" ]; then
    curl -s -b session "$INPUT_FILE_URL" > "$INPUT_FILE_PATH"
    EXIT_CODE=$?
    if [ $EXIT_CODE -ne 0 ]; then
        echo "Failed to download input file from $INPUT_FILE_URL."
        exit $EXIT_CODE
    fi
    echo "Successfully downloaded the input file."
fi

SOLUTION_FILE_PATH="$DAY.py"
if [ ! -f "$SOLUTION_FILE_PATH" ]; then
    title=$(curl -s -b session "https://adventofcode.com/2022/day/$DAY" | grep -o -P '(?<=<h2>--- ).*(?= ---</h2>)')
    cat <<EOT > $SOLUTION_FILE_PATH
import utils


DAY = $DAY
TITLE = '$title'


def procress_input(input: list[str]):
    pass


def print_solutions(data):
    # utils.print_sol_part(PART_NR, VALUE)
    pass


def main():
    utils.print_title(TITLE)
    lines = utils.read_input(DAY)
    data = procress_input(lines)
    print_solutions(data)


if __name__ == '__main__':
    main()

EOT
fi

echo "Day $DAY ready for coding..."
code "$SOLUTION_FILE_PATH"
