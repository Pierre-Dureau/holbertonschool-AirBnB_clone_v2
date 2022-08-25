# Web server preparation with puppet

exec { 'update':
  command => '/usr/bin/apt-get update'
}

exec { 'install':
  command => '/usr/bin/apt-get -y install nginx'
}

exec { 'mkdir':
  command => '/usr/bin/mkdir -p /data/web_static/releases/test/'
}

exec { 'mkdir2':
  command => '/usr/bin/mkdir -p /data/web_static/shared/'
}

exec { 'echo':
  command => '/usr/bin/echo "Holberton School" > /data/web_static/releases/test/index.html'
}

exec { 'ln':
  command => '/usr/bin/ln -sf /data/web_static/releases/test/ /data/web_static/current'
}

exec { 'chown':
  command => '/usr/bin/chown -R ubuntu:ubuntu /data/'
}

exec { 'sed':
  command => '/usr/bin/sed -i "47i location /hbnb_static {alias /data/web_static/current/; }" /etc/nginx/sites-available/default'
}

exec { 'restart':
  command => '/usr/sbin/service nginx restart'
}
