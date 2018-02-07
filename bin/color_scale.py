#!/usr/bin/python3

from colour import Color


def get_scaled_color(value):
    start_color = Color('green')
    end_color = Color('red')
    colors = list(start_color.range_to(end_color, 101))

    value = int(value)

    return colors[value]


def get_temperature_color(value):
    start_color = Color('green')
    end_color = Color('red')
    colors = list(start_color.range_to(end_color, 101))

    value = int(value)

    return colors[value]
