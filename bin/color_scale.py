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
    if value == 90:
        return "FF0EF0"
    if value == 89:
        return "FF0DF0"
    if value == 88:
        return "FF0CF0"
    if value == 87:
        return "FF0BF0"
    if value == 86:
        return "FF0AF0"
    if value == 85:
        return "FF09F0"
    if value == 84:
        return "FF08F0"
    if value == 83:
        return "FF07F0"
    if value == 82:
        return "FF06F0"
    if value == 81:
        return "FF05F0"
    if value == 80:
        return "FF04F0"
    if value == 79:
        return "FF03F0"
    if value == 78:
        return "FF02F0"
    if value == 77:
        return "FF01F0"
    if value == 76:
        return "FF00F0"
    if value == 75:
        return "FF00E0"
    if value == 74:
        return "FF00D0"
    if value == 73:
        return "FF00C0"
    if value == 72:
        return "FF00B0"
    if value == 71:
        return "FF00A0"
    if value == 70:
        return "FF0090"
    if value == 69:
        return "FF0080"
    if value == 68:
        return "FF0070"
    if value == 67:
        return "FF0060"
    if value == 66:
        return "FF0050"
    if value == 65:
        return "FF0040"
    if value == 64:
        return "FF0030"
    if value == 63:
        return "FF0020"
    if value == 62:
        return "FF0010"
    if value == 61:
        return "FF0000"
    if value == 60:
        return "FF0a00"
    if value == 59:
        return "FF1400"
    if value == 58:
        return "FF1e00"
    if value == 57:
        return "FF2800"
    if value == 56:
        return "FF3200"
    if value == 55:
        return "FF3c00"
    if value == 54:
        return "FF4600"
    if value == 53:
        return "FF5000"
    if value == 52:
        return "FF5a00"
    if value == 51:
        return "FF6400"
    if value == 50:
        return "FF6e00"
    if value == 49:
        return "FF7800"
    if value == 48:
        return "FF8200"
    if value == 47:
        return "FF8c00"
    if value == 46:
        return "FF9600"
    if value == 45:
        return "FFa000"
    if value == 44:
        return "FFaa00"
    if value == 43:
        return "FFb400"
    if value == 42:
        return "FFbe00"
    if value == 41:
        return "FFc800"
    if value == 40:
        return "FFd200"
    if value == 39:
        return "FFdc00"
    if value == 38:
        return "FFe600"
    if value == 37:
        return "FFf000"
    if value == 36:
        return "FFfa00"
    if value == 35:
        return "fdff00"
    if value == 34:
        return "d7ff00"
    if value == 33:
        return "b0ff00"
    if value == 32:
        return "8aff00"
    if value == 31:
        return "65ff00"
    if value == 30:
        return "3eff00"
    if value == 29:
        return "17ff00"
    if value == 28:
        return "00ff10"
    if value == 27:
        return "00ff36"
    if value == 26:
        return "00ff5c"
    if value == 25:
        return "00ff83"
    if value == 24:
        return "00ffa8"
    if value == 23:
        return "00ffd0"
    if value == 22:
        return "00fff4"
    if value == 21:
        return "00e4ff"
    if value == 20:
        return "00d4ff"
    if value == 19:
        return "00c4ff"
    if value == 18:
        return "00b4ff"
    if value == 17:
        return "00a4ff"
    if value == 16:
        return "0094ff"
    if value == 15:
        return "0084ff"
    if value == 14:
        return "0074ff"
    if value == 13:
        return "0064ff"
    if value == 12:
        return "0054ff"
    if value == 11:
        return "0044ff"
    if value == 10:
        return "0032ff"
    if value == 9:
        return "0022ff"
    if value == 8:
        return "0012ff"
    if value == 7:
        return "0002ff"
    if value == 6:
        return "0000ff"
    if value == 5:
        return "0100ff"
    if value == 4:
        return "0200ff"
    if value == 3:
        return "0300ff"
    if value == 2:
        return "0400ff"
    if value == 1:
        return "0500ff"
