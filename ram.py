#!/usr/bin/python3

import psutil


def sizeof_fmt(num, suffix='B'):
    for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)


def get_ram():
    ram = psutil.virtual_memory()
    ram_used = (ram.total - ram.available)
    ram_total = ram.total

    print('$stippled_hr\n RAM$alignr %(used)s / %(total)s\n$stippled_hr\n' % {'used': sizeof_fmt(ram_used),
                                                                              'total': sizeof_fmt(ram_total)})
    print('$membar')
