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
    'cpu': {
        'start': 'FFFF00',
        'end': 'FFFF00'
    },
    'temperature': {
        'start': 'FF0000',
        'end': 'FF0000'
    },
    'bars': 'FFFFFF',
    'graphs': {
        'gradient1': 'FFFFFF',
        'gradient2': 'FFFFFF'
    },
    'docker': {
        'running': 'ADFF2F',
        'stopped': 'FF0000',
        'restarting': 'ADFF2F',
        'paused': 'FF0000',
        'default': 'FFFFFF'
    }
}
