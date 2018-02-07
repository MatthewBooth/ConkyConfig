#!/usr/bin/python3

import bin.cpu as cpu
import bin.disks as disks
import bin.docker_containers as containers
import bin.network as network
import bin.ram as ram
import bin.system as system
import bin.temps as temps


def __main__():
    system.__main__()
    cpu.__main__()
    ram.__main__()
    temps.__main__()
    disks.__main__()
    network.__main__()
    containers.__main__()


__main__()
