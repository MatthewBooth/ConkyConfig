#!/usr/bin/python3

import os


def uptime():
    try:
        f = open("/proc/uptime")
        contents = f.read().split()
        f.close()
    except:
        return "Cannot open uptime file: /proc/uptime"

    total_seconds = float(contents[0])

    # Helper vars:
    MINUTE = 60
    HOUR = MINUTE * 60
    DAY = HOUR * 24

    # Get the days, hours, etc:
    days = int(total_seconds / DAY)
    hours = int((total_seconds % DAY) / HOUR)
    minutes = int((total_seconds % HOUR) / MINUTE)
    seconds = int(total_seconds % MINUTE)

    # Build up the pretty string (like this: "N days, N hours, N minutes, N seconds")
    string = ""
    if days > 0:
        string += str(days) + "D "
    if len(string) > 0 or hours > 0:
        string += str(hours) + "H "
    if len(string) > 0 or minutes > 0:
        string += str(minutes) + "M "
    string += str(seconds) + "S"

    return string


def get_system():
    uname = os.uname()

    print('$stippled_hr\n%(user)s - %(os)s %(kernel)s (%(arch)s)\n$stippled_hr\n' % {'user': uname.nodename,
                                                                                     'os': uname.sysname,
                                                                                     'kernel': uname.release,
                                                                                     'arch': uname.machine})

    print("Kernel: $alignr %(kernel)s" % {'kernel': uname.release})
    print("Uptime: $alignr %(time)s" % {'time': uptime()})
