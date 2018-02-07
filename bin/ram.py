#!/usr/bin/python3

import psutil
from bin.utils import sizeof_fmt


def __get_ram():
    ram = psutil.virtual_memory()
    ram_used = (ram.total - ram.available)
    ram_total = ram.total

    print('$stippled_hr\n RAM$alignr %(used)s / %(total)s\n$stippled_hr\n' % {'used': sizeof_fmt(ram_used),
                                                                              'total': sizeof_fmt(ram_total)})
    print('$membar')


def __main__():
    __get_ram()
