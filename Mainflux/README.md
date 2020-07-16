
cd mainflux/

Запуск mainflux (sudo fuser -k 1883/tcp - освободить порт n)

  1. sudo make run

Запуск mainflux-cli
  
  1. wget https://github.com/mainflux/mainflux/releases/downloa.. 16:03:43— https://github.com/mainflux/mainflux/releases/downloa..

  2. tar xvf mainflux-cli_v0.11.0_linux-amd64.tar.gz

  2 ./mainflux-cli

  3 ./mainflux-cli users create Julia_Zhirnova@email.com password

  4 ./mainflux-cli users token Julia_Zhirnova@email.com password

  4 export USERTOKEN=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1OTQ5NjE5NjEsImlhdCI6MTU5NDkyNTk2MSwiaXNzIjoibWFpbmZsdXguYXV0aG4iLCJzdWIiOiJKdWxpYV9aaGlybm92YUBlbWFpbC5jb20iLCJ0eXBlIjowfQ.FiPlrT9a8mZYJ5HpoV17q4NnI4aP93vQc-j49bCfo6w

  5 ./mainflux-cli things create '{"type":"device", "name":"myThing"}' $USERTOKEN

  6 ./mainflux-cli things create '{"type":"app", "name":"ChatBot"}' $USERTOKEN

  7 ./mainflux-cli things get all $USERTOKEN
  
{
  "limit": 100,
  "offset": 0,
  "things": [
    {
      "id": "273ddb40-8fc9-4c6e-b60a-c35e9f42f51d",
      "key": "eaaac5c0-71f9-47bd-b7a3-6badb8213662",
      "name": "ChatBot"
    },
    {
      "id": "38e4965c-8a02-4835-875c-761475944aff",
      "key": "ff0616cc-75e4-43a7-a94d-22e7e7bc7843",
      "name": "myThing"
    }
  ],
  "total": 2
}

  8 ./mainflux-cli channels create '{"name":"l"}' $USERTOKEN

  9 ./mainflux-cli channels get all $USERTOKEN
  
{
  "channels": [
    {
      "id": "8ae3c0e6-e338-4b3e-b52a-fedcb439702a",
      "name": "l"
    }
  ],
  "limit": 100,
  "offset": 0,
  "total": 1
}

  10 ./mainflux-cli things connect 273ddb40-8fc9-4c6e-b60a-c35e9f42f51d 8ae3c0e6-e338-4b3e-b52a-fedcb439702a $USERTOKEN
                                                (id у things 1)                 (id у channels)

  11 ./mainflux-cli things connect 38e4965c-8a02-4835-875c-761475944aff 8ae3c0e6-e338-4b3e-b52a-fedcb439702a $USERTOKEN
                                                (id у things 2)                 (id у channels)

    Запуск mqtt_sub

  1. export THINGTOKEN=eaaac5c0-71f9-47bd-b7a3-6badb8213662 ("key" у things 1)

  2. mosquitto_sub -u 273ddb40-8fc9-4c6e-b60a-c35e9f42f51d -P $THINGTOKEN -t channels/8ae3c0e6-e338-4b3e-b52a-fedcb439702a/messages
                                              (id у things 1)                 (id у channels)

    Запуск mqtt_pub

1. export THINGTOKEN=14c500ec-b657-4c36-8d08-cc00d01e61e4 ("key" у things 2)

2.  mosquitto_pub -u 38e4965c-8a02-4835-875c-761475944aff -P $THINGTOKEN -t channels/8ae3c0e6-e338-4b3e-b52a-fedcb439702a/messages -m "Hello ;)"
                                                (id у things 2)                 (id у channels)

Удаление 
 
 1. ./mainflux-cli things delete f4d497a5-f152-47f8-b101-0610f6ea4a20 $USERTOKEN
 
 2. ./mainflux-cli things delete f91806e4-fecd-408e-bd79-dd8f04a73579 $USERTOKEN
 
 3. ./mainflux-cli channels delete e923ab60-90c7-4df9-9091-4f1c726dee84 $USERTOKEN
 
 Удаляем контейнеры sudo docker rm -f $(sudo docker ps -aq)

 Удаляем изображения sudo docker rmi -f $(sudo docker images -q)


