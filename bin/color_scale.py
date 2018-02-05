#!/usr/bin/python3


def get_scaled_color(value):
    value = int(value)
    if 0 <= value <= 10:
        return '${color 17ff00}'
    elif 10 <= value <= 19:
        return '${color 3fff00}'
    elif 20 <= value <= 29:
        return '${color 67ff00}'
    elif 30 <= value <= 39:
        return '${color 8eff00}'
    elif 40 <= value <= 49:
        return '${color b6ff00}'
    elif 50 <= value <= 59:
        return '${color deff00}'
    elif 60 <= value <= 69:
        return '${color fff900}'
    elif 70 <= value <= 79:
        return '${color ffd100}'
    elif 80 <= value <= 89:
        return '${color ffa900}'
    elif 90 <= value <= 99:
        return '${color ff8100}'
    else:
        return '${color ffffff}'


def get_temperature_color(value):
    value = int(value)
    if 0 <= value <= 29:
        return '${color 17ff00}'
    elif 29 <= value <= 38:
        return '${color 3fff00}'
    elif 38 <= value <= 42:
        return '${color 67ff00}'
    elif 42 <= value <= 46:
        return '${color 8eff00}'
    elif 46 <= value <= 50:
        return '${color b6ff00}'
    elif 50 <= value <= 54:
        return '${color deff00}'
    elif 54 <= value <= 58:
        return '${color fff900}'
    elif 58 <= value <= 62:
        return '${color ffd100}'
    elif 58 <= value <= 62:
        return '${color ffa900}'
    elif 58 <= value <= 62:
        return '${color ff8100}'
    elif 58 <= value <= 62:
        return '${color ff5900}'
    elif 58 <= value <= 62:
        return '${color ff3200}'
    else:
        return '${color ff0a00}'
