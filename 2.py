import utils


DAY = 2
TITLE = 'Day 2: Rock Paper Scissors'


class RPS:
    OPPONENT_ROCK = 'A'
    OPPONENT_PAPER = 'B'
    OPPONENT_SCISSORS = 'C'

    # part 1
    PICK_ROCK = 'X'
    PICK_PAPER = 'Y'
    PICK_SCISSORS = 'Z'

    # part 2
    RESULT_WIN = 'Z'
    RESULT_DRAW = 'Y'
    RESULT_LOSE = 'X'


def round_score1(round: str) -> int:
    opponent, me = round.split(' ')
    score = 0
    score += shape_score(me)
    score += outcome_score(opponent, me)
    return score


def round_score2(round: str) -> int:
    opponent, result = round.split(' ')
    me = me_choose(opponent, result)
    score = 0
    score += shape_score(me)
    score += outcome_score(opponent, me)
    return score


def shape_score(shape: str):
    match shape:
        case RPS.PICK_ROCK:
            return 1
        case RPS.PICK_PAPER:
            return 2
        case RPS.PICK_SCISSORS:
            return 3
        case _:
            return 0


def outcome_score(opponent: str, me: str):
    match (opponent, me):
        case (RPS.OPPONENT_ROCK, RPS.PICK_PAPER) | (RPS.OPPONENT_PAPER, RPS.PICK_SCISSORS) | (RPS.OPPONENT_SCISSORS, RPS.PICK_ROCK):
            return 6
        case (RPS.OPPONENT_ROCK, RPS.PICK_ROCK) | (RPS.OPPONENT_PAPER, RPS.PICK_PAPER) | (RPS.OPPONENT_SCISSORS, RPS.PICK_SCISSORS):
            return 3
        case _:
            return 0


def me_choose(opponent: str, result: str):
    match (opponent, result):
        case (RPS.OPPONENT_ROCK, RPS.RESULT_DRAW) | (RPS.OPPONENT_PAPER, RPS.RESULT_LOSE) | (RPS.OPPONENT_SCISSORS, RPS.RESULT_WIN):
            return RPS.PICK_ROCK
        case (RPS.OPPONENT_ROCK, RPS.RESULT_WIN) | (RPS.OPPONENT_PAPER, RPS.RESULT_DRAW) | (RPS.OPPONENT_SCISSORS, RPS.RESULT_LOSE):
            return RPS.PICK_PAPER
        case (RPS.OPPONENT_ROCK, RPS.RESULT_LOSE) | (RPS.OPPONENT_PAPER, RPS.RESULT_WIN) | (RPS.OPPONENT_SCISSORS, RPS.RESULT_DRAW):
            return RPS.PICK_SCISSORS


def procress_input(input: list[str]):
    game_score1 = sum(map(round_score1, input))
    game_score2 = sum(map(round_score2, input))
    return (game_score1, game_score2)


def print_solutions(data: tuple[int, int]):
    utils.print_sol_part(1, data[0])
    utils.print_sol_part(2, data[1])


def main():
    utils.print_title(TITLE)
    lines = utils.read_input(DAY)
    data = procress_input(lines)
    print_solutions(data)


if __name__ == '__main__':
    main()
