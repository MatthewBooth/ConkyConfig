#!/usr/bin/python3

from colour import Color as Colour


def get_scaled_color(value):
    start_color = Colour('white')
    end_color = Colour('red')
    colors = list(start_color.range_to(end_color, 101))

    value = int(value)

    return colors[value]


def get_temperature_color(value):
    start_color = Colour('green')
    end_color = Colour('red')
    colors = list(start_color.range_to(end_color, 70))

    value = int(value - 20)

    return colors[value]
