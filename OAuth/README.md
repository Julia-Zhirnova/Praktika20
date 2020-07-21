   Для запуска докера:

      остановить базу данных
      sudo service influxdb stop

      остановить сервер mqtt
      /etc/init.d/mosquitto stop

      sudo xhost +
      sudo docker-compose build
      sudo docker-compose up -d
   
   Cоздаем пользователя и получаем токен

      curl -d "usern=ulia&passw=paparatata" 0.0.0.0:8011/user 

      {"status":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoidWxpYSIsIm5taHMiOiIwZjMxM2M5YjY4MTQ4MDMwMDg3NWJjZTI2ZmE5YjE0ODMyNTMyZmM1OWJlZTg2ZDZlODZhMWY5OTU4Nzk1MDhiIiwic2VjIjoiaWVpZWllaWFhYWFhYWFvb28xMjQxMDI0azEyMCIsInJhbmRvbSI6IjAuMDA5NzQzMDAyNDg2Nzc2MTc2In0.pw6nbeITQkpFXyxds9VaV3Rc4d9JQFkAw-G6TkkpgzI"}

      создаем переменную
      curl -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoidWxpYSIsIm5taHMiOiIwZjMxM2M5YjY4MTQ4MDMwMDg3NWJjZTI2ZmE5YjE0ODMyNTMyZmM1OWJlZTg2ZDZlODZhMWY5OTU4Nzk1MDhiIiwic2VjIjoiaWVpZWllaWFhYWFhYWFvb28xMjQxMDI0azEyMCIsInJhbmRvbSI6IjAuOTcxMzk4MzU5MTk4MTk3NiJ9.2xh8jXkpph95ctqX1lkoTaLy_f31MkUvewgMntkC2mc" "0.0.0.0:8011/mosq?top=ee&name=qq"
      задаем ее значение
      mosquitto_pub -m "1.73" -t "ee/qq"
      mosquitto_pub -m "3.14" -t "ee/qq"
      mosquitto_pub -m "2.3" -t "ee/qq"
      mosquitto_pub -m "5.6" -t "ee/qq"
  
      curl -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoidWxpYSIsIm5taHMiOiIwZjMxM2M5YjY4MTQ4MDMwMDg3NWJjZTI2ZmE5YjE0ODMyNTMyZmM1OWJlZTg2ZDZlODZhMWY5OTU4Nzk1MDhiIiwic2VjIjoiaWVpZWllaWFhYWFhYWFvb28xMjQxMDI0azEyMCIsInJhbmRvbSI6IjAuOTcxMzk4MzU5MTk4MTk3NiJ9.2xh8jXkpph95ctqX1lkoTaLy_f31MkUvewgMntkC2mc" "0.0.0.0:8011/mosq?top=ee&name=ab"
      mosquitto_pub -m "2.3" -t "ee/ab"
      mosquitto_pub -m "1.3" -t "ee/ab"

      curl -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoidWxpYSIsIm5taHMiOiIwZjMxM2M5YjY4MTQ4MDMwMDg3NWJjZTI2ZmE5YjE0ODMyNTMyZmM1OWJlZTg2ZDZlODZhMWY5OTU4Nzk1MDhiIiwic2VjIjoiaWVpZWllaWFhYWFhYWFvb28xMjQxMDI0azEyMCIsInJhbmRvbSI6IjAuOTcxMzk4MzU5MTk4MTk3NiJ9.2xh8jXkpph95ctqX1lkoTaLy_f31MkUvewgMntkC2mc" "0.0.0.0:8011/mosq?top=lm&name=work"
      mosquitto_pub -m "5.5" -t "lm/work"
      mosquitto_pub -m "7.5" -t "lm/work"

      проверяем их наличие
      127.0.0.1:8011/list
      выводит
      count	3
         val	
         ab	2.3
         qq	5.6
         work	5.5

      запускаем сервер 
      http://127.0.0.1:8011/start (выведет сообщение Started)

      строим графики python3 -m prog.graph

      останавливаем сервер 
      http://127.0.0.1:8011/stop (выведет сообщение Stopped)

      Удаляем контейнеры sudo docker rm -f $(sudo docker ps -aq)

      Удаляем изображения sudo docker rmi -f $(sudo docker images -q)
