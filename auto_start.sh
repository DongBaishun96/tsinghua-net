# !/bin/bash

username=""
password=""
read -p "Please input the user name :" username

if [ "${username}" = "" ]; then
    echo "Error: empty of user name."
    exit
fi

read -p "Please input the password :" password

if [ "${password}" = "" ]; then
    echo "Error: empty of password."
    exit
fi

apt install expect -y

service_conf="
[Unit] \n
Description=TsinghuaNet \n
After=network.target \n
\n 
[Service] \n
Type=simple \n
User=root \n
Restart=on-failure \n
RestartSec=5s \n
ExecStart=/bin/sh -c 'unbuffer tsinghua_net schedule -u ${username} -p ${password} 2>&1 > /var/log/tsinghua-net.log' \n
ExecReload=/bin/sh -c 'unbuffer tsinghua_net schedule -u ${username} -p ${password} 2>&1 > /var/log/tsinghua-net.log' \n
\n
[Install] \n
WantedBy=multi-user.target \n
"

echo -e $service_conf > /etc/systemd/system/tsinghua_net.service

systemctl daemon-reload
systemctl stop tsinghua_net.service
systemctl start tsinghua_net.service
systemctl enable tsinghua_net.service

echo "Enable tsinghua_net.service success."