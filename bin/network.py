#!/usr/bin/python3

import netifaces


def get_network():
    interface = netifaces.gateways()['default'][netifaces.AF_INET][1]
    print('$stippled_hr\nNetwork\n$stippled_hr\n')
    print(
        'Down$alignc ${downspeed %(interface)s}$color$alignr ${totaldown %(interface)s}' % {'interface': interface})
    print('${downspeedgraph %(interface)s}' % {'interface': interface})
    print('Up$alignc ${upspeed %(interface)s}$color$alignr ${totalup %(interface)s}' % {'interface': interface})
    print('${upspeedgraph %(interface)s}' % {'interface': interface})
