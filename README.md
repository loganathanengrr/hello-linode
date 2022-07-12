```

sudo useradd -m logan
sudo passwd logan

-------- Add Group ---
sudo groupadd www-data
sudo usermod -a -G www-data logan
grep www-data /etc/group

---- Create-Dir ---
mkdir -p /var/www/
mkdir -p /var/www-logs
mkdir -p /var/www-git

--- Changing owenership ---
sudo chgrp -R www-data /var/www
sudo chgrp -R www-data /var/www-logs
sudo chgrp -R www-data /var/www-git

---- Giving permission ---
sudo chmod -R g+rwxs /var/www/
sudo chmod -R g+rwxs /var/www-logs/
sudo chmod -R g+rwxs /var/www-git/

--- Add user SSH login ---
sudo adduser new_user
sudo adduser new_user --disabled-password
sudo su - new_user
mkdir .ssh
chmod 700 .ssh
touch .ssh/authorized_keys
chmod 600 .ssh/authorized_keys
ssh keygen -y -- enter the path for the private key
copy public to authorized_keys
ssh -i /path/new_key_pair.pem new_user@public_dns_name_of_EC2_Linux_instance

---- Installation ---
sudo apt update
sudo apt install ufw nginx

---- Firewall -----
sudo ufw allow ssh
sudo ufw enable
sudo ufw allow 'Nginx Full' -- this will allow the port 80 and 443

---- After Nginx installations ---
sudo chgrp -R www-data /var/www/html/
sudo chmod -R g+rwxs /var/www/html


---- Installation GIT ---
sudo apt install git -y
git config --global init.defaultBranch main

---Conf of GIT---
mkdir hello-ec2-fastapi.git
cd //
git init --bare

--- Local--
git remote add ec2 ssh://logan@3.86.205.246:/var/www-git/hello-ec2-fastapi.git
git push ec2 main
git remote -v

--- Error---
cd ~/.ssh/config and add:


Host example
Hostname example.com
User myuser
IdentityFile ~/.ssh/other_id_rsa

---- Post Recive --
cd hooks
touch post-receive
nano post-receive
chmod +x post-receive
#!/bin/bash

#git --dest --source checkout main -f
git --work-tree=/var/www/ --git-dir=/var/www-git/hello-ec2-fastapi.git checkout main -f
pkill -HUP gunicorn


--- Setup for Python --
mkdir app
cd app
touch main.py
--- commit the code ---
python3 -m virtualenv .

-- add to this gitignore
bin/
lib/
include/
pyvenv.cfg

--- install---
pip install fastapi
push the changes to remote machine

---- install remote machine---
through root user

sudo apt update
sudo apt install python3-pip python3-venv python3-dev -y

--through logan user
go the app directory
python3 -m venv .
. bin/activate
pip intall fastapi

---add to req.txt file--
jinja2
uvicorn
gunicorn
 install these items


--- update the code main.py
-- push to ec2
-- run it again

--after nginx conf push vm--
through root user
cp /var/www/nginx/myapp.conf /etc/nginx/sites-available
cd ..
cd sites-enabled
rm default
sudo systemctl reload nginx
ln -s /etc/nginx/sites-available/myapp.conf /etc/nginx/sites-enabled/myapp.conf
sudo systemctl reload nginx

gunicorn -k uvicorn.workers.UvicornWorker main:app --bind 0.0.0.0:8000

for kill -- pkill -HUP gunicorn --- This will sending signal to gunicorn to stop

--- install supervisor on VM
through root after pusing supervisor conf
sudo apt update
sudo apt install supervisor -y
sudo supervisor start
sudo supervisorctl status
cp /var/www/supervisor/myapp.supervisor.conf /etc/supervisor/conf.d
sudo supervisorctl reread
sudo supervisorctl update
 ---
add pkill -HUP gunicorn into post-receive

```