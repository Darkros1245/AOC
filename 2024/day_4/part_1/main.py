type Position = tuple[int, int]
type Direction = tuple[int, int]


XMAS = "XMAS"


def get_neighbors(
    x: int, y: int, board: list[str]
) -> list[tuple[str, Position, Direction]]:
    return [
        (board[y + _y][x + _x], (y + _y, x + _x), (_y, _x))
        for _y in range(-1, 2)
        for _x in range(-1, 2)
        if 0 <= x + _x < len(board[0])
        and 0 <= y + _y < len(board)
        and not (_x == 0 and _y == 0)
    ]


def is_this_xmas(
    c: str,
    expected: int,
    direction: tuple[int, int] | None,
    x: int,
    y: int,
    board: list[str],
) -> int:
    if c != XMAS[expected]:
        return 0

    if XMAS[expected] == XMAS[-1]:
        return 1

    if direction is not None:
        return (
            is_this_xmas(
                board[y + direction[0]][x + direction[1]],
                expected + 1,
                direction,
                x + direction[1],
                y + direction[0],
                board,
            )
            if 0 <= x + direction[1] < len(board[0])
            and 0 <= y + direction[0] < len(board)
            else 0
        )

    return sum(
        [
            is_this_xmas(
                neighbor[0],
                expected + 1,
                neighbor[2],
                neighbor[1][1],
                neighbor[1][0],
                board,
            )
            for neighbor in get_neighbors(x, y, board)
        ]
    )


def main(lines: list[str]) -> None:
    total = 0
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            total += is_this_xmas(c, 0, None, x, y, lines)
    print(total)


if __name__ == "__main__":
    with open("../input.txt") as file:
        lines = "".join([line for line in file.readlines()]).strip().split("\n")
    main(lines)
