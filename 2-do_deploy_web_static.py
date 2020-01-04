#!/usr/bin/python3
from fabric.api import *
from datetime import datetime
import os

env.hosts = ['35.227.56.7', '35.231.96.229']
env.user = 'ubuntu'


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder
    of AirBnB clone.
    """
    try:
        if not os.path.exists("./versions"):
            local("mkdir versions")
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "web_static_" + date + ".tgz"
        command = "tar -cvzf " + "./versions/" + file_name + " ./web_static"
        local(command)
        return "versions/" + file_name
    except:
        return None


def do_deploy(archive_path):
    """Distributes an archive to your web servers.
    """
    if archive_path is None:
        return False

    # Upload archive to servers /tmp/ dir
    upload = put(archive_path, '/tmp/')
    if upload.failed:
        return False

    # Building path based on given archive path (contains .tgz extension)
    new_path = archive_path.split('/')[-1]
    folder = new_path.split('.')[0]

    # Create folder
    command = 'mkdir -p /data/web_static/releases/{}'.format(folder)
    stat = run(command)
    if stat.failed:
        return False

    # Uncompress archive and clean up
    command = 'tar -xzf /tmp/{} '.format(new_path)
    command += '-C /data/web_static/releases/{}'.format(folder)
    run(command)
    run('rm -rf /tmp/{}'.format(new_path))
    command = 'mv /data/web_static/releases/{}/web_static/* '.format(folder)
    command += '/data/web_static/releases/{}/'.format(folder)
    run(command)
    cleanup = 'rm -rf /data/web_static/releases/{}/web_static'.format(folder)
    run(cleanup)

    # Delete old sym link and create a new one
    run('rm -rf /data/web_static/current')
    command = 'ln -s /data/web_static/releases/{}/ '.format(folder)
    command += '/data/web_static/current'
    run(command)
    return True
