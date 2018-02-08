#!/usr/bin/python3
import textwrap

import psutil

from bin.utils import sizeof_fmt
from config.config import colors


def __get_ram():
    ram = psutil.virtual_memory()
    ram_used = (ram.total - ram.available)
    ram_total = ram.total

    bar_color = colors['bars']

    ram_output = textwrap.dedent("""\
    $stippled_hr
    RAM$alignr %(used)s / %(total)s
    $stippled_hr
    """)

    print(ram_output % {'used': sizeof_fmt(ram_used), 'total': sizeof_fmt(ram_total)})
    print('${color %(color)s}$membar{$color}' % {'color': bar_color})


def __main__():
    __get_ram()
