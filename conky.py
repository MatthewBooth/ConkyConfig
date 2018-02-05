#!/usr/bin/python3

import sys
from cpu import get_cpu
from system import get_system
from ram import get_ram
from temps import get_temps
from disks import get_disks
from network import get_network
from docker_containers import get_docker


def run():
    get_system()
    get_cpu()
    get_ram()
    get_temps()
    get_disks()
    get_network(sys.argv[1])
    get_docker()


run()
