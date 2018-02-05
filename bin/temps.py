#!/usr/bin/python3
# coding=utf-8

import psutil
import py3nvml.nvidia_smi as nvml


def get_temps():
    __get_cpu_temps()
    __get_gpu_temps()


def __get_scaled_color(value):
    if 0 <= value <= 29:
        return '${color 17ff00}'
    elif 34 <= value <= 38:
        return '${color 3fff00}'
    elif 38 <= value <= 42:
        return '${color 67ff00}'
    elif 42 <= value <= 46:
        return '${color 8eff00}'
    elif 46 <= value <= 50:
        return '${color b6ff00}'
    elif 50 <= value <= 54:
        return '${color deff00}'
    elif 54 <= value <= 58:
        return '${color fff900}'
    elif 58 <= value <= 62:
        return '${color ffd100}'
    elif 58 <= value <= 62:
        return '${color ffa900}'
    elif 58 <= value <= 62:
        return '${color ff8100}'
    elif 58 <= value <= 62:
        return '${color ff5900}'
    elif 58 <= value <= 62:
        return '${color ff3200}'
    else:
        return '${color ff0a00}'


def __get_gpu_temps():
    nvml.nvmlInit()

    device_count = nvml.nvmlDeviceGetCount()

    print('\nGPU:')
    if device_count > 0:
        for i in range(device_count):
            gpu_temp = nvml.nvmlDeviceGetTemperature(nvml.nvmlDeviceGetHandleByIndex(i), 0)
            print(' GPU %(i)s: ${alignr}%(color)s%(temp)s${color}°C' % {
                'i': i,
                'color': __get_scaled_color(gpu_temp),
                'temp': gpu_temp
            })
    nvml.nvmlShutdown()


def __get_cpu_temps():
    temps_list = list(psutil.sensors_temperatures()['coretemp'])
    cpu_temp = int(temps_list[0].current)

    print('$stippled_hr\nTemperatures\n$stippled_hr\n')
    print('CPU: ${alignr}%(color)s%(temp)s${color}°C' % {
        'color': __get_scaled_color(cpu_temp),
        'temp': cpu_temp
    })

    for item in range(1, 5):
        core_temp = int(temps_list[item].current)
        print(' Core %(i)s: ${alignr}%(color)s%(temp)s${color}°C' % {
            'i': item,
            'color': __get_scaled_color(core_temp),
            'temp': core_temp
        })
