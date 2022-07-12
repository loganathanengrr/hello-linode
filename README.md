```
Python
FASTAPI
NGINX
GUNICORN
GIT
SUPERVISOR
SQL- (POSTGRESQL)
REDIS- ()
LOAD BALANCER

Cloud Infra--Linode



sudo useradd -m logan
sudo passwd logan


sudo groupadd www-data
sudo usermod -a -G www-data logan
grep www-data /etc/group

mkdir -p /var/www
mkdir -p /var/www-git
mkdir -p /var/www-logs

# Changing Ownership

sudo chgrp -R www-data /var/www
sudo chgrp -R www-data /var/www-git
sudo chgrp -R www-data /var/www-logs

# Provides Permissions

sudo chmod -R g+rwxs /var/www
sudo chmod -R g+rwxs /var/www-git
sudo chmod -R g+rwxs /var/www-logs

cp root/authorized_keys <user>/.ssh/authorized_keys

sudo apt update
sudo apt install nginx ufw -y
sudo ufw allow ssh
sudo ufw enable
sudo ufw allow 'Nginx Full'





```