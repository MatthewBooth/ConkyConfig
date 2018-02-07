#!/usr/bin/python3
import textwrap

import psutil


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

    # Loop over the partitions and draw each one as a bar with usage stats
    for p in partitions_list:
        # Root will not show as / unless we intervene
        name = p.mountpoint
        if name == '/':
            label = 'Root'
        else:
            label = name
        # Ignore Docker mounts
        if "docker" not in name:
            disk_output = textwrap.dedent("""\
            %(label)s ${alignr}${fs_used %(name)s}B / ${fs_size %(name)s}B
            ${fs_bar %(name)s}
            """)
            print(disk_output % {'label': label, 'name': name})


def __main__():
    __get_disks()
