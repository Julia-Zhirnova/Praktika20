sudo xhost +
sudo docker-compose build
sudo docker-compose up -d
sudo docker-compose run —rm runme /bin/bash
chmod +x start.sh && ./start.sh
