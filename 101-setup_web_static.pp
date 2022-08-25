# Web server preparation with puppet

exec { 'update':
  command => 'apt-get update',
  path    => '/usr/bin',
}

package { 'nginx':
  ensure  => present,
  name    => 'nginx',
  require => Exec['update'],
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

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
