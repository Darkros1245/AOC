with open("../input.txt") as file:
    print(
        sum(
            (lambda _list: [x * _list[1].count(x) for x in _list[0]])(
                list(
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
                    )
                )
            )
        )
    )
