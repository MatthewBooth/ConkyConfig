#!/usr/bin/python3
import textwrap

import psutil

import bin.utils as utils
import config.config as config


def __get_disks():
    # Get a list of all partitions on the device
    partitions_list = list(psutil.disk_partitions(all=False))

    # Print the header
    header = textwrap.dedent("""\
                $stippled_hr
                Disks
                $stippled_hr
                """)
    print(header)

    exclude_list = config.config['disks']['exclude']

    bar_color = config.colors['bars']

    # Loop over the partitions and draw each one as a bar with usage stats
    for p in partitions_list:
        # Root will not show as / unless we intervene
        name = p.mountpoint

        # Exclude items in the exclude list
        exclude = False
        for e in exclude_list:
            if utils.full_match(e, name):
                exclude = True

        if exclude is True:
            continue

        # Set the label name
        if name == '/':
            label = 'Root'
        else:
            label = name

        # Write the data
        disk_output = textwrap.dedent("""\
        %(label)s ${alignr}${fs_used %(name)s}B / ${fs_size %(name)s}B
        ${color %(color)s}${fs_bar %(name)s}{$color}
        """)
        print(disk_output % {'label': label, 'name': name, 'color': bar_color})


def __main__():
    __get_disks()
