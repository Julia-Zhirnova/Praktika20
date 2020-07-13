Для запуска докера:

остановить базу данных
sudo service influxdb stop
остановить сервер mqtt
/etc/init.d/mosquitto stop

sudo xhost +
sudo docker-compose build
sudo docker-compose up -d

В интернет ввести:

http://127.0.0.1:8011/start (выведет сообщение Started)

http://127.0.0.1:8011/list - (переменных пока нет, выведет сообщение {"len": 0, "vars": {}})

Добавлять переменные через API http://127.0.0.1:8011/add?name=ab&bv=1 (выведет сообщение OK) 
Проверить, что добавились http://127.0.0.1:8011/list (выведет сообщение {"len": 4, "vars": {"ab": -0.1577185161713195,})

Для запуска таймера, в консоли ввести:
  python3 -m dbselect -h (выведет сообщение о доступных командах)
  python3 -m dbselect -d tsdb -m measurement_tsdb -t "15:14:00 13/07/2020"  (выведет все данные о переменных с указанного времени)
  python3 -m dbselect -d tsdb -m measurement_tsdb -t "15:14:00 13/07/2020"  --ps 1 (выведет изменения за 1с)

В интернет ввести:

Удаляем переменные http://127.0.0.1:8011/del?name=ab&bv=1 (выведет сообщение OK) 

Проверить, что удалилось http://127.0.0.1:8011/list (переменных нет, выведет сообщение {"len": 0, "vars": {}})

http://127.0.0.1:8011/stop (выведет сообщение Stopped)

Удаляем контейнеры sudo docker rm -f $(sudo docker ps -aq)

Удаляем изображения sudo docker rmi -f $(sudo docker images -q)
