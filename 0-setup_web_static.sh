#!/usr/bin/env bash
# Prepare the web servers
apt-get update
apt-get -y install nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "Holberton School" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
chgrp -R ubuntu:ubuntu /data/
sed -i '/server_name _;/a \\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}' /etc/nginx/sites-available/default
service nginx restart
