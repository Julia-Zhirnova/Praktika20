sudo service influxdb stop 

Для запуска докера:
 1. sudo xhost +
 2. sudo docker-compose build
 3. sudo docker-compose up -d
 4. sudo docker-compose run —rm runme /bin/bash
 5. chmod +x start.sh && ./start.sh
 
Удаляем контейнеры
sudo docker rm -f $(sudo docker ps -aq)
Удаляем изображения
sudo docker rmi -f $(sudo docker images -q)
