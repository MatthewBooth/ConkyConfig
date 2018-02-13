#!/usr/bin/python3

from colour import Color as Colour

from config.config import colors
from config.config import config


def get_cpu_usage_color(value):
    temp_color = colors['gpu']

    current = int(value)
    high = config['gpu']['levels']['high']
    critical = config['gpu']['levels']['critical']

    return __get_ranged_color(critical, current, high, temp_color)


def get_cpu_temps_color(temps):
    temp_color = colors['temperature']
    current = int(temps.current)
    critical = int(temps.critical)
    high = int(temps.high)

    return __get_ranged_color(critical, current, high, temp_color)


def get_gpu_temps_color(temp):
    temp_color = colors['gpu']

    current = int(temp)
    high = config['gpu']['levels']['high']
    critical = config['gpu']['levels']['critical']

    return __get_ranged_color(critical, current, high, temp_color)


def __get_ranged_color(critical, current, high, temp_color):
    if current >= critical:
        return temp_color['critical']
    elif current >= high:
        return temp_color['high']
    else:
        start_color = Colour('#' + temp_color['start'])
        end_color = Colour('#' + temp_color['end'])
        color_list = list(start_color.range_to(end_color, high))

        value = int(current)

        return color_list[value]
