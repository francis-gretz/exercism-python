def steps(number: int):
    if not isinstance(number, int):
        raise ValueError("Only positive integers are allowed")
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    steps = 0
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = (number * 3) + 1
        steps += 1

    return steps


print(steps(12))
print(steps(25555555))
