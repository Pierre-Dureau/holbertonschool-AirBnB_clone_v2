# Web server preparation with puppet

exec { 'update':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure  => 'present',
  name    => 'nginx',
  require => Exec['update'],
}

exec { 'mkdir':
  command => 'mkdir -p /data/web_static/releases/test/'
  path => '/usr/bin'
}

exec { 'mkdir2':
  command => 'mkdir -p /data/web_static/shared/'
  path => '/usr/bin'
}

exec { 'echo':
  command => 'echo "Holberton School" > /data/web_static/releases/test/index.html'
  path => '/usr/bin'
}

exec { 'ln':
  command => 'ln -sf /data/web_static/releases/test/ /data/web_static/current'
  path => '/usr/bin'
}

exec { 'chown':
  command => 'chown -R ubuntu:ubuntu /data/'
  path => '/usr/bin'
}

exec { 'sed':
  command => 'sed -i '47i\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}' /etc/nginx/sites-available/default'
  path => '/usr/bin'
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
