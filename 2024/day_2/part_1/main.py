from functools import reduce

with open("../input.txt") as file:
    print(
        len(
            [
                safe
                for safe, _ in map(
                    lambda record: reduce(
                        lambda state, levels: (
                            state[0]
                            and (
                                (state[1] and 1 <= levels[1] - levels[0] <= 3)
                                or (not state[1] and 1 <= levels[0] - levels[1] <= 3)
                            ),
                            state[1],
                        ),
                        [record[i : i + 2] for i in range(len(record) - 1)],
                        (True, record[0] < record[1]),
                    ),
                    filter(
                        lambda record: record,
                        map(
                            lambda line: [
                                int(level.strip())
                                for level in line.split(" ")
                                if level != "\n"
                            ],
                            file.readlines(),
                        ),
                    ),
                )
                if safe
            ]
        )
    )