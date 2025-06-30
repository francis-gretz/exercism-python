COLORS = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
]


def value(colors):
    result = int(color_code(colors[0])) * 10
    result += int(color_code(colors[1]))

    return result


def color_code(color):
    return COLORS.index(color)


def power_of_ten(power):
    return 10 ** power


def get_metric_suffix(ohms):
    if ohms > 1_000_000_000:
        prefix = "giga"
        ohms //= 1_000_000_000
    elif ohms > 1_000_000:
        prefix = "mega"
        ohms //= 1_000_000
    elif ohms > 1_000:
        prefix = "kilo"
        ohms //= 1_000
    else:
        prefix = ""

    return f"{ohms} {prefix}ohms"


def label(colors):
    colors_value = value(colors)
    zeroes = int(color_code(colors[2]))

    colors_value *= power_of_ten(zeroes)

    return get_metric_suffix(colors_value)
