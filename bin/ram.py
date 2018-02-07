#!/usr/bin/python3
import textwrap

import psutil

from bin.utils import sizeof_fmt


def __get_ram():
    ram = psutil.virtual_memory()
    ram_used = (ram.total - ram.available)
    ram_total = ram.total

    ram_output = textwrap.dedent("""\
    $stippled_hr
    RAM$alignr %(used)s / %(total)s
    $stippled_hr
    """)

    print(ram_output % {'used': sizeof_fmt(ram_used), 'total': sizeof_fmt(ram_total)})
    print('$membar')


def __main__():
    __get_ram()
