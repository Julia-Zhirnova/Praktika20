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
    
    Добавлять переменные через MQTT http://127.0.0.1:8011/mqtt?name=cd&topic=var (выведет сообщение Variable Added for MQTT) 
                                    http://127.0.0.1:8011/mqtt?name=ef&topic=var (выведет сообщение Variable Added for MQTT) 

В консоли задать значения переменных mosquitto_pub -m "1.73" -t "var/cd"   mosquitto_pub -m "3.813" -t "var/cd"
                                     mosquitto_pub -m "3.1415" -t "var/ef"   mosquitto_pub -m "4.2426" -t "var/ef"

    python3 graph.py - построит графики

В интернет ввести:

    Удаляем переменные http://127.0.0.1:8011/del?name=ab&bv=1 (выведет сообщение OK) 
    
    Проверить, что удалилось http://127.0.0.1:8011/list (переменных нет, выведет сообщение {"len": 0, "vars": {}})
    
    http://127.0.0.1:8011/stop (выведет сообщение Stopped)

Удаляем контейнеры sudo docker rm -f $(sudo docker ps -aq)

Удаляем изображения sudo docker rmi -f $(sudo docker images -q)
