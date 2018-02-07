#!/usr/bin/python3

import textwrap

import docker


def __get_docker():
    client = docker.from_env()

    container_list = client.containers.list()
    if len(container_list) != 0:
        # Print the header
        header = textwrap.dedent("""\
                        $stippled_hr
                        Docker
                        $stippled_hr
                        """)
        print(header)
        for container in container_list:
            if container.status == 'running' or container.status == 'restarting':
                color = 'ADFF2F'
            elif container.status == 'paused' or container.status == 'stopped':
                color = 'FF0000'
            else:
                color = 'FFFFFF'
            docker_output = textwrap.dedent("%(container)s ${alignr}${color %(color)s}%(status)s${color}")
            print(docker_output % {
                'container': container.name,
                'color': color,
                'status': container.status
            })


def __main__():
    __get_docker()
