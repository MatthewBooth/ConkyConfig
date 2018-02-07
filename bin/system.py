#!/usr/bin/python3

import os
import textwrap

from bin.utils import uptime


def __get_system():
    uname = os.uname()
    header = textwrap.dedent("""\
    $stippled_hr
    %(user)s - %(os)s %(kernel)s (%(arch)s)
    $stippled_hr
    """)

    print(header % {
        'user': uname.nodename,
        'os': uname.sysname,
        'kernel': uname.release,
        'arch': uname.machine
    })

    print("Kernel: $alignr %(kernel)s" % {'kernel': uname.release})
    print("Uptime: $alignr %(time)s" % {'time': uptime()})


def __main__():
    __get_system()
