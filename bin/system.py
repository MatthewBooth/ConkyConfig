#!/usr/bin/python3

import os
from bin.utils import uptime


def __get_system():
    uname = os.uname()

    print('$stippled_hr\n%(user)s - %(os)s %(kernel)s (%(arch)s)\n$stippled_hr\n' % {'user': uname.nodename,
                                                                                     'os': uname.sysname,
                                                                                     'kernel': uname.release,
                                                                                     'arch': uname.machine})

    print("Kernel: $alignr %(kernel)s" % {'kernel': uname.release})
    print("Uptime: $alignr %(time)s" % {'time': uptime()})


def __main__():
    __get_system()
