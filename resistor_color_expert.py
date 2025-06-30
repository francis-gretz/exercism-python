COLORS = [
    "black",   # 0
    "brown",   # 1
    "red",     # 2
    "orange",  # 3
    "yellow",  # 4
    "green",   # 5
    "blue",    # 6
    "violet",  # 7
    "grey",    # 8
    "white",   # 9
]


TOLERANCE_BAND = {
    "grey": "±0.05%",
    "violet": "±0.1%",
    "blue": "±0.25%",
    "green": "±0.5%",
    "brown": "±1%",
    "red": "±2%",
    "gold": "±5%",
    "silver": "±10%",
}


def value(colors):
    length_colors = len(colors)

    result = 0
    result += int(color_code(colors[0]))
    if (length_colors >= 4):
        result = (result * 10) + int(color_code(colors[1]))
    if (length_colors >= 5):
        result = (result * 10) + int(color_code(colors[2]))

    return result


def color_code(color):
    return COLORS.index(color)


def power_of_ten(power):
    return 10 ** power


def get_tolerance_value(colors):
    length_colors = len(colors)

    if (length_colors < 3):
        return str("")

    tolerance = TOLERANCE_BAND.get(colors[length_colors - 1])

    return " " + tolerance


def get_metric_suffix(ohms):
    if ohms >= 1_000_000_000:
        prefix = "giga"
        ohms /= 1_000_000_000
    elif ohms >= 1_000_000:
        prefix = "mega"
        ohms /= 1_000_000
    elif ohms >= 1_000:
        prefix = "kilo"
        ohms /= 1_000
    else:
        prefix = ""

    return f"{int(ohms) if ohms == int(ohms) else ohms} {prefix}ohms"


def label(colors):
    length_colors = len(colors)

    ohms = value(colors)

    if length_colors > 2:
        zeroes = int(color_code(colors[length_colors - 2]))
    else:
        zeroes = 0

    ohms *= power_of_ten(zeroes)

    return get_metric_suffix(ohms) + get_tolerance_value(colors)


def resistor_label(colors):
    return label(colors)
