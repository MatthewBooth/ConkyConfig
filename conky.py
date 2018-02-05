#!/usr/bin/python3

import sys
from bin.cpu import get_cpu
from bin.system import get_system
from bin.ram import get_ram
from bin.temps import get_temps
from bin.disks import get_disks
from bin.network import get_network
from bin.docker_containers import get_docker


def run():
    get_system()
    get_cpu()
    get_ram()
    get_temps()
    get_disks()
    get_network(sys.argv[1])
    get_docker()


run()
