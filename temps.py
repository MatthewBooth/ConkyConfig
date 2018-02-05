#!/usr/bin/python3

import psutil


def get_temps():
    temps_list = list(psutil.sensors_temperatures()['coretemp'])
    color_low = '${color FFFFFF}'
    color_mid = '${color FF7F50}'
    color_high = '${color FF0000}'

    print('$stippled_hr\nTemperatures\n$stippled_hr\n')
    print('CPU: ${alignr}%(temp)s°C' % {'temp': int(temps_list[0].current)})
    for item in range(1, 5):
        if 0 >= item <= 33:
            color = color_low
        elif 34 >= item <= 66:
            color = color_mid
        else:
            color = color_high
        print(' Core %(i)s: ${alignr}%(color)s%(temp)s${color}°C' % {'i': item, 'color': color,
                                                                     'temp': int(temps_list[item].current)})
