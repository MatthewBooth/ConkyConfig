#!/usr/bin/python3

import sys


def get_network(interface):
    if len(sys.argv) >= 2:
        print('$stippled_hr\nNetwork\n$stippled_hr\n')
        print(
            'Down$alignc ${downspeed %(interface)s}$color$alignr ${totaldown %(interface)s}' % {'interface': interface})
        print('${downspeedgraph %(interface)s}' % {'interface': interface})
        print('Up$alignc ${upspeed %(interface)s}$color$alignr ${totalup %(interface)s}' % {'interface': interface})
        print('${upspeedgraph %(interface)s}' % {'interface': interface})
