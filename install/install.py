#!/usr/bin/python3
import errno
import os

import jinja2


def __write_text_to_file(content, file):
    if os.path.exists(file):
        f = open(file, 'w+')
    else:
        f = open(file, 'x')

    f.write(content)
    f.close()


def __render_jinja_template(tpl_path, variables):
    path, filename = os.path.split(tpl_path)
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(path or './')
    ).get_template(filename).render(variables)


def __write_supervisor_conf(user):
    user_variables = {
        'user': user
    }

    result = __render_jinja_template('install/supervisor.conky.conf.j2', user_variables)

    supervisor_conf_file = '/etc/supervisor/conf.d/conky.conf'

    __write_text_to_file(result, supervisor_conf_file)


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


def run():
    user = os.getlogin()
    __write_supervisor_conf(user)
    __symlink_conkyrc(user)


run()
