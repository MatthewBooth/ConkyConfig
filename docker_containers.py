#!/usr/bin/python3

import docker


def get_docker():
    client = docker.from_env()

    container_list = client.containers.list()
    if len(container_list) != 0:
        print('$stippled_hr\n Docker\n$stippled_hr\n')
        for container in container_list:
            if container.status == 'running' or container.status == 'restarting':
                color = 'ADFF2F'
            elif container.status == 'paused' or container.status == 'stopped':
                color = 'FF0000'
            else:
                color = 'FFFFFF'
            print('%(container)s ${alignr}${color %(color)s}%(status)s${color}' % {'container': container.name,
                                                                                   'color': color,
                                                                                   'status': container.status})
