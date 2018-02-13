#!/usr/bin/python3
import os

from fcache.cache import FileCache

import bin.cpu as cpu
import bin.disks as disks
import bin.docker_containers as containers
import bin.network as network
import bin.ram as ram
import bin.system as system
import bin.temps as temps


def __main__():
    conky_path = os.path.dirname(os.path.realpath(__file__))
    cache_path = conky_path + '/.cache'

    # Create cache
    cache = FileCache('conky_cache', flag='cs', app_cache_dir=cache_path)
    cache.create()

    system.__main__()
    cpu.__main__()
    ram.__main__()
    temps.__main__()
    disks.__main__()
    network.__main__()
    containers.__main__()

    # Close Cache
    cache.close()


__main__()
