# 00001 = wink
# 00010 = double blink
# 00100 = close your eyes
# 01000 = jump
# 10000 = Reverse the order of the operations in the secret handshake.

def add_result(result, index):
    match index:
        case 4:
            result.append("wink")
            return result

        case 3:
            result.append("double blink")
            return result

        case 2:
            result.append("close your eyes")
            return result

        case 1:
            result.append("jump")
            return result

        case 0:
            result.reverse()
            return result


def commands(binary_str):
    result = []

    for index in range(4, -1, -1):
        if binary_str[index] == '1':
            result = add_result(result, index)
    return result


print(commands("10011"))
