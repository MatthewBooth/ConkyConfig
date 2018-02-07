#!/usr/bin/python3

import netifaces


def __get_network():
    default_gateways = netifaces.gateways()['default']
    if len(default_gateways) != 0:
        interface = default_gateways[netifaces.AF_INET][1]
        print('$stippled_hr\nNetwork\n$stippled_hr\n')
        print(
            'Down$alignc ${downspeed %(interface)s}$color$alignr ${totaldown %(interface)s}' % {'interface': interface})
        print('${downspeedgraph %(interface)s}' % {'interface': interface})
        print('Up$alignc ${upspeed %(interface)s}$color$alignr ${totalup %(interface)s}' % {'interface': interface})
        print('${upspeedgraph %(interface)s}' % {'interface': interface})


def __main__():
    __get_network()
