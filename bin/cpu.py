#!/usr/bin/python3

import psutil


def get_cpu():
    cpu_percent_list = list(psutil.cpu_percent(interval=1, percpu=True))
    cpu_freq = psutil.cpu_freq(percpu=False)

    color_low = '${color FFFFFF}'
    color_mid = '${color FF7F50}'
    color_high = '${color FF4500}'

    if len(cpu_percent_list) != 0:
        print('$stippled_hr\n CPU${alignr}%(freq)s MHz\n$stippled_hr\n' % {'freq': int(cpu_freq.current)})
        for num, cpu in enumerate(cpu_percent_list, start=1):
            if 0 <= cpu <= 33:
                color = color_low
            elif 34 <= cpu <= 66:
                color = color_mid
            else:
                color = color_high

            print('CPU %(num)s:${alignr}%(color)s%(cpu)s${color}%%' % {'num': num, 'color': color, 'cpu': str(cpu)})

    print('$cpugraph')
