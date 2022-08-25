#!/usr/bin/python3
"""Fabric file for packaging"""
from fabric.operations import *
from datetime import datetime
from os.path import exists

env.hosts = ['54.173.31.188', '3.80.45.187']


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


def do_deploy(archive_path):
    """deploy an archive to your web servers"""
    if exists(archive_path) is False:
        return False

    file_tgz = archive_path.split('/')[1]
    file_name = file_tgz.split('.')[0]
    p_rls = '/data/web_static/releases/'

    cmd = put(str(archive_path), "/tmp/{}".format(file_tgz))
    if cmd.failed is True:
        return False

    cmd = run("mkdir -p {}{}/".format(p_rls, file_name))
    if cmd.failed is True:
        return False

    cmd = run("tar -xzf /tmp/{} -C {}{}".format(file_tgz, p_rls, file_name))
    if cmd.failed is True:
        return False

    cmd = run("rm /tmp/{}".format(file_tgz))
    if cmd.failed is True:
        return False

    cmd = run("mv {}{}/web_static/* {}{}/"
              .format(p_rls, file_name, p_rls, file_name))
    if cmd.failed is True:
        return False

    cmd = run("rm -rf {}{}/web_static".format(p_rls, file_name))
    if cmd.failed is True:
        return False

    cmd = run("rm -rf /data/web_static/current")
    if cmd.failed is True:
        return False

    cmd = run("ln -s {}{}/ /data/web_static/current".format(p_rls, file_name))
    if cmd.failed is True:
        return False

    print("New version deployed!")
    return True


def deploy():
    """creates and deploy an archive to your web servers"""
    archive = do_pack()
    if archive is None:
        return False
    return do_deploy(archive)


def do_clean(number=0):
    """deletes out-of-date archives"""
    n = int(number)
    if n == 0:
        n = 1
    files = local("ls -1t versions/", capture=True)
    files_list = files.split('\n')
    size = len(files_list)
    for i in range(n, size):
        local("rm versions/{}".format(files_list[i]))

    files = run("ls -1t /data/web_static/releases")
    files_list = files.split('\n')
    i = 0
    for files in files_list:
        i += 1
        if i == 1 or files == 'test':
            continue
        run("rm -rf /data/web_static/releases/{}".format(files))
