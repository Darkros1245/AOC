with open("../input.txt") as file:
    print(
        sum(
            map(
                lambda x: abs(x[0] - x[1]),
                zip(
                    *map(
                        lambda x: sorted(x),
                        zip(
                            *filter(
                                lambda x: x,
                                map(
                                    lambda line: [
                                        int(num.strip())
                                        for num in line.split("   ")
                                        if num != "\n"
                                    ],
                                    file.readlines(),
                                ),
                            )
                        ),
                    )
                ),
            )
        )
    )
