sudo curl -L "https://github.com/docker/compose/releases/download/v2.24.6/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo chmod -R 777 data/
sudo mkdir -p data/bookkeeper/ledgers/current
sudo chmod -R 777 data/bookkeeper/ledgers/current
sudo mkdir -p data/bookkeeper/journal/current
sudo chmod -R 777 data/bookkeeper/journal/current