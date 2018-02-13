#!/usr/bin/python3

import textwrap

import docker

from config.config import colors


def __get_docker():
    docker_colors = colors['docker']
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
            if (
                    container.status == 'running'
                    or container.status == 'restarting'
                    or container.status == 'paused'
                    or container.status == 'stopped'
            ):
                color = docker_colors[container.status]
            else:
                color = docker_colors['default']
            docker_output = textwrap.dedent("%(container)s ${alignr}${color %(color)s}%(status)s${color}")
            print(docker_output % {
                'container': container.name,
                'color': color,
                'status': container.status
            })


def __main__():
    __get_docker()
