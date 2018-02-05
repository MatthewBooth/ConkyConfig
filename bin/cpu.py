#!/usr/bin/python3

import psutil
from bin.color_scale import get_scaled_color


def get_cpu():
    cpu_percent_list = list(psutil.cpu_percent(interval=1, percpu=True))
    cpu_freq = psutil.cpu_freq(percpu=False)

    if len(cpu_percent_list) != 0:
        print('$stippled_hr\n CPU${alignr}%(freq)s MHz\n$stippled_hr\n' % {'freq': int(cpu_freq.current)})
        for num, cpu in enumerate(cpu_percent_list, start=1):
            print('CPU %(num)s:${alignr}%(color)s%(cpu)s${color}%%' % {'num': num, 'color': get_scaled_color(cpu), 'cpu': str(cpu)})

    print('$cpugraph')
