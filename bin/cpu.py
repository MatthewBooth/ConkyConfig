#!/usr/bin/python3
import textwrap

import psutil

from bin.color_scale import get_cpu_usage_color
from config.config import colors


def __get_cpu():
    # Get all of the CPU cores in a list with their percentage values
    cpu_percent_list = list(psutil.cpu_percent(interval=0.5, percpu=True))
    # GEt the overall CPU frequency
    cpu_freq = psutil.cpu_freq(percpu=False)

    if len(cpu_percent_list) != 0:
        # Print the header
        print(textwrap.dedent("""\
        $stippled_hr
        CPU${alignr}%(freq)s MHz
        $stippled_hr
        """) % {
            'freq': int(cpu_freq.current)
        })
        # Loop over the cores and print out their percentage used
        for num, cpu in enumerate(cpu_percent_list, start=1):
            print("CPU %(num)s:${alignr}${color %(color)s}%(cpu)s${color}%%" % {
                'num': num,
                'color': get_cpu_usage_color(int(cpu)),
                'cpu': str(int(cpu))
            })
        # Draw the CPU graph
        colors_graphs = colors['graphs']
        print('${cpugraph cpu0 30,0 %(color1)s %(color2)s s -t}'
              % {'color1': colors_graphs['gradient1'], 'color2': colors_graphs['gradient2']}
              )


def __main__():
    __get_cpu()
