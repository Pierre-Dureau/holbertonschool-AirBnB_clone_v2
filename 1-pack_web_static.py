#!/usr/bin/python3
"""Fabric file for packaging"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Pack all web_static files"""
    local("mkdir -p versions")
    date = datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')
    path = 'versions/web_static_' + date + '.tgz'
    cmd = local("tar -cvzf {} web_static".format(path))
    if cmd.succeeded:
        return path
    else:
        return None
