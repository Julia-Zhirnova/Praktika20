Для запуска докера:
    sudo service influxdb stop
    sudo xhost +
    sudo docker-compose build
    sudo docker-compose up -d
    
В интернет ввести:
    http://127.0.0.1:8011/start (выведет сообщение Started)
    http://127.0.0.1:8011/list - (переменных пока нет, выведет сообщение {"len": 0, "vars": {}})
    Добавлять переменные
    http://127.0.0.1:8011/add?name=ab&bv=1 (выведет сообщение OK)
    http://127.0.0.1:8011/add?name=cd&bv=2 (выведет сообщение OK)
    http://127.0.0.1:8011/add?name=ef&bv=3 (выведет сообщение OK)
    http://127.0.0.1:8011/add?name=gh&bv=4 (выведет сообщение OK)
    Проверить, что добавились
    http://127.0.0.1:8011/list 
    (выведет сообщение {"len": 4, "vars": {"ab": -0.1577185161713195, "cd": -0.11154436724256478, "ef": -0.046377088325095905, "gh": 1.7205230119906192}})
    
Запустить в консоли python3 graph.py - построит графики

В интернет ввести:
    Удаляем переменные
    http://127.0.0.1:8011/del?name=ab&bv=1 (выведет сообщение OK)
    http://127.0.0.1:8011/del?name=cd&bv=2 (выведет сообщение OK)
    http://127.0.0.1:8011/del?name=ef&bv=3 (выведет сообщение OK)
    http://127.0.0.1:8011/del?name=gh&bv=4 (выведет сообщение OK)
    Проверить, что удалилось
    http://127.0.0.1:8011/list (переменных нет, выведет сообщение {"len": 0, "vars": {}})
    http://127.0.0.1:8011/stop (выведет сообщение Stopped)
    sudo docker-compose run —rm runme /bin/bash
    chmod +x start.sh && ./start.sh

Удаляем контейнеры
sudo docker rm -f $(sudo docker ps -aq)
Удаляем изображения
sudo docker rmi -f $(sudo docker images -q)
