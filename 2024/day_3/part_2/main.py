import re

with open("../input.txt") as file:
    print(
        sum(
            [
                int(x[0]) * int(x[1])
                for xs in [
                    re.findall(r"mul\(([0-9]+),([0-9]+)\)", line)
                    for line in map(
                        lambda x: x.split("don't")[0],
                        re.split(
                            r"do[^n]", "".join([line for line in file.readlines()])
                        ),
                    )
                ]
                for x in xs
            ]
        )
    )
