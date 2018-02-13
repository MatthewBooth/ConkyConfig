#!/usr/bin/python3

config = {
    'disks': {
        'exclude': [
            "^/boot/.*$",
            "^/var/lib/docker/.*$"
        ]
    },
    'cpu': {
        'levels': {
            'high': 70,
            'critical': 90
        }
    },
    'gpu': {
        'levels': {
            'high': 70,
            'critical': 90
        }
    }
}

colors = {
    'cpu': {
        'start': 'FFFFFF',
        'end': '008000',
        'high': 'FF4500',
        'critical': 'FF0000'
    },
    'gpu': {
        'start': 'FFFFFF',
        'end': '008000',
        'high': 'FF4500',
        'critical': 'FF0000'
    },
    'temperature': {
        'start': 'FFFFFF',
        'end': '008000',
        'high': 'FF4500',
        'critical': 'FF0000'
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
