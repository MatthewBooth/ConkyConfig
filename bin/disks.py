#!/usr/bin/python3

import psutil


def get_disks():
    partitions_list = list(psutil.disk_partitions(all=False))

    print('$stippled_hr\nDisks\n$stippled_hr\n')

    for p in partitions_list:
        name = p.mountpoint
        if name == '/':
            label = 'Root'
        else:
            label = name
        if "docker" not in name:
            print(
                '%(label)s ${alignr}${fs_used %(name)s}B / ${fs_size %(name)s}B\n${fs_bar %(name)s}' % {'label': label,
                                                                                                        'name': name})
