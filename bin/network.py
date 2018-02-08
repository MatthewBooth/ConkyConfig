#!/usr/bin/python3

import netifaces
import textwrap
from config.config import colors

def __get_network():
    # Get the default gateways
    default_gateways = netifaces.gateways()['default']

    # Only show the network code if there is at least one gateway active
    if len(default_gateways) != 0:
        # Get the name of the gateway that is using IPv4
        interface = default_gateways[netifaces.AF_INET][1]
        interface_type = interface[:2]

        # Print the header
        if interface_type == "en":
            # With Ethernet
            header = textwrap.dedent("""\
            $stippled_hr
            Network
            $stippled_hr
            """)
        else:
            # With WiFi
            header = textwrap.dedent("""\
            $stippled_hr
            Network${alignc}$wireless_essid}${alignr}${wireless_link_qual_perc %(interface)s}%%
            $stippled_hr
            """)

        print(header % {'interface': interface})

        colors_graphs = colors['graphs']

        # Show the graphs and bitrates
        network_output = textwrap.dedent("""\
        Down$alignc ${downspeed %(interface)s}$color$alignr ${totaldown %(interface)s}
        ${downspeedgraph %(interface)s 30,0 %(color1)s %(color2)s s -t}
        Up$alignc ${upspeed %(interface)s}$color$alignr ${totalup %(interface)s}
        ${upspeedgraph %(interface)s 30,0 %(color1)s %(color2)s s -t}
        """)
        print(network_output % {'interface': interface, 'color1': colors_graphs['gradient1'], 'color2': colors_graphs['gradient2']})


def __main__():
    __get_network()
