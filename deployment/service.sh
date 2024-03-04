 sudo vim /etc/systemd/system/docker-compose-app.service


[Unit]
Description=Docker Compose Application Service
Requires=docker.service
After=docker.service

[Service]
Type=oneshot
RemainAfterExit=yes
WorkingDirectory=/home/ja_riverao1uniandes
ExecStart=sudo /usr/local/bin/docker-compose --profile pulsar start
ExecStop=sudo /usr/local/bin/docker-compose --profile pulsar stop
TimeoutStartSec=0

[Install]
WantedBy=multi-user.target


sudo systemctl daemon-reload
sudo systemctl enable docker-compose-app.service
sudo systemctl start docker-compose-app.service
sudo systemctl status docker-compose-app.service
