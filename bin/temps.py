#!/usr/bin/python3
# coding=utf-8
import textwrap

import psutil
from py3nvml import py3nvml as nvml

import bin.utils as utils
from bin.color_scale import get_cpu_temps_color
from bin.color_scale import get_gpu_temps_color


def __get_gpu_temps():
    if utils.which('nvidia-smi') is not None:
        try:
            nvml.nvmlInit()
        except nvml.NVMLError as e:
            pass
        else:
            device_count = nvml.nvmlDeviceGetCount()
            print('\nGPU:')
            if device_count > 0:
                for i in range(device_count):
                    handle = nvml.nvmlDeviceGetHandleByIndex(i)
                    gpu_temp = nvml.nvmlDeviceGetTemperature(handle, 0)
                    print(' GPU %(i)s: ${alignr}${color %(color)s}%(temp)s${color}°C' % {
                        'i': i,
                        'color': get_gpu_temps_color(gpu_temp),
                        'temp': gpu_temp
                    })
            nvml.nvmlShutdown()


def __get_cpu_temps():
    # Only run when sensors is installed and is feeding data
    if utils.which('sensors') is not None:
        # Create a list of CPU temperatures
        temps_list = list(psutil.sensors_temperatures()['coretemp'])

        # Overall CPU temp
        cpu_temp = int(temps_list[0].current)
        print('CPU: ${alignr}${color %(color)s}%(temp)s${color}°C' % {
            'color': get_cpu_temps_color(temps_list[0]),
            'temp': cpu_temp
        })

        # Loop over the items in the temperature list to print core temps
        for item in range(1, len(temps_list)):
            core_temp = temps_list[item]
            print(' Core %(i)s: ${alignr}${color %(color)s}%(temp)s${color}°C' % {
                'i': item,
                'color': get_cpu_temps_color(core_temp),
                'temp': int(core_temp.current)
            })


def __main__():
    header = textwrap.dedent("""\
                            $stippled_hr
                            Temperatures
                            $stippled_hr
                            """)
    print(header)
    __get_cpu_temps()
    __get_gpu_temps()
