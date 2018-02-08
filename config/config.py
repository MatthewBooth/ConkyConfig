#!/usr/bin/python3

config = {
    'disks': {
        'exclude': [
            "^/boot/.*$",
            "^/var/lib/docker/.*$"
        ]
    }
}

colors = {
    'bars': '',
    'graphs': {
        'gradient1': '',
        'gradient2': ''
    },
    'docker': {
        'running': 'ADFF2F',
        'stopped': 'FF0000',
        'restarting': 'ADFF2F',
        'paused': 'FF0000',
        'default': 'FFFFFF'
    }
}
