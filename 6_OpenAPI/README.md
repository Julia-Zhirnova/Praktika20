Для запуска докера:
   1. sudo service influxdb stop
   2. sudo xhost +
   3. sudo docker-compose build
   4. sudo docker-compose up -d
    
В интернет ввести:

  1.  http://127.0.0.1:8011/start (выведет сообщение Started)
  2.  http://127.0.0.1:8011/list - (переменных пока нет, выведет сообщение {"len": 0, "vars": {}})
  3.  Добавлять переменные
    http://127.0.0.1:8011/add?name=name&bv=1 (выведет сообщение OK)
    http://127.0.0.1:8011/add?name=ab&bv=2 (выведет сообщение OK)
        
  4.  Проверить, что добавились
    http://127.0.0.1:8011/list 
    (выведет сообщение {"count":2,"val":{"ab":-0.2718735549378192,"name":1.8504780539420451}})
    
Запустить в консоли python3 graph.py - построит графики

В интернет ввести:

   1. Удаляем переменные
    http://127.0.0.1:8011/del?name=ab&bv=1 (выведет сообщение OK)
    http://127.0.0.1:8011/del?name=cd&bv=2 (выведет сообщение OK)
    http://127.0.0.1:8011/del?name=ef&bv=3 (выведет сообщение OK)
    http://127.0.0.1:8011/del?name=gh&bv=4 (выведет сообщение OK)
    
   2. Проверить, что удалилось
    http://127.0.0.1:8011/list (переменных нет, выведет сообщение {"len": 0, "vars": {}})
    http://127.0.0.1:8011/stop (выведет сообщение Stopped)
    
Удаляем контейнеры
 sudo docker rm -f $(sudo docker ps -aq)

Удаляем изображения
 sudo docker rmi -f $(sudo docker images -q)
