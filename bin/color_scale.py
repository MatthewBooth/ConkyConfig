#!/usr/bin/python3

from colour import Color as Colour
from config.config import colors


def get_scaled_color(value):
    cpu_color = colors['cpu']
    start_color = Colour('#' + cpu_color['start'])
    end_color = Colour('#' + cpu_color['end'])
    color_list = list(start_color.range_to(end_color, 101))

    value = int(value)

    return color_list[value]


def get_temperature_color(value):
    temp_color = colors['temperature']
    start_color = Colour('#' + temp_color['start'])
    end_color = Colour('#' + temp_color['end'])
    color_list = list(start_color.range_to(end_color, 100))

    value = int(value)

    return color_list[value]
