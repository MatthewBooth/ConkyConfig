#!/usr/bin/python3
import argparse
import errno
import os

import jinja2


def __render_jinja_template(tpl_path, variables):
    path, filename = os.path.split(tpl_path)
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(path or './')
    ).get_template(filename).render(variables)


def __write_supervisor_conf(user):
    user_variables = {
        'user': user
    }

    result = __render_jinja_template('install.conky.conf.j2', user_variables)

    supervisor_conf_file = '/etc/install/conf.d/conky.conf'

    f = open(supervisor_conf_file, 'w')
    f.write(result)


def __symlink_conkyrc(user):
    user_folder = ("/home/%(user)s" % {'user': user})
    config = user_folder + "/.conky/conky_config.lua"
    rc_file = user_folder + '/.conkyrc'
    try:
        os.symlink(config, rc_file)
    except OSError as e:
        if e.errno == errno.EEXIST:
            os.remove(rc_file)
            os.symlink(config, rc_file)


parser = argparse.ArgumentParser()
parser.add_argument("username", help="Your current username", type=str)
args = parser.parse_args()

if args.username is not "":
    __write_supervisor_conf(args.username)
    __symlink_conkyrc(args.username)
else:
    print(args)
