
Запуск mainflux

  1. sudo make run

Запуск mainflux-cli
  
  1. wget https://github.com/mainflux/mainflux/releases/downloa.. 16:03:43— https://github.com/mainflux/mainflux/releases/downloa..
tar xvf mainflux-cli_v0.11.0_linux-amd64.tar.gz

  2 ./mainflux-cli

  3 ./mainflux-cli users create john.doe@email.com password

  4 ./mainflux-cli users token john.doe@email.com password
export USERTOKEN=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1OTQ5NDIxNjMsImlhdCI6MTU5NDkwNjE2MywiaXNzIjoibWFpbmZsdXguYXV0aG4iLCJzdWIiOiJqb2huLmRvZUBlbWFpbC5jb20iLCJ0eXBlIjowfQ.rlb_xTOgoJRgiFIAW5M2S-xzKXJpDG2vwGatihA-3mY

  5 ./mainflux-cli things create '{"type":"device", "name":"myThing"}' $USERTOKEN

  6 ./mainflux-cli things create '{"type":"app", "name":"testapp"}' $USERTOKEN

  7 ./mainflux-cli things get all $USERTOKEN
  
  {
  "limit": 100,
  "offset": 0,
  "things": [
    {
      "id": "f4d497a5-f152-47f8-b101-0610f6ea4a20",
      "key": "387d3d63-df61-4294-ba87-6c29cc2998a2",
      "name": "testapp"
    },
    {
      "id": "f91806e4-fecd-408e-bd79-dd8f04a73579",
      "key": "14c500ec-b657-4c36-8d08-cc00d01e61e4",
      "name": "myThing"
    }
  ],
  "total": 2
}

  8 ./mainflux-cli channels create '{"name":"myChannel"}' $USERTOKEN

  9 ./mainflux-cli channels get all $USERTOKEN
  
  {
  "channels": [
    {
      "id": "e923ab60-90c7-4df9-9091-4f1c726dee84",
      "name": "myChannel"
    }
  ],
  "limit": 100,
  "offset": 0,
  "total": 1
}


  10 ./mainflux-cli things connect f4d497a5-f152-47f8-b101-0610f6ea4a20 e923ab60-90c7-4df9-9091-4f1c726dee84 $USERTOKEN
                                                (id у things 1)                 (id у channels)

  11 ./mainflux-cli things connect f91806e4-fecd-408e-bd79-dd8f04a73579 e923ab60-90c7-4df9-9091-4f1c726dee84 $USERTOKEN
                                                (id у things 2)                 (id у channels)
Запуск mqtt_sub

  1. export THINGTOKEN=387d3d63-df61-4294-ba87-6c29cc2998a2 ("key" у things 1)

  2. mosquitto_sub -u f4d497a5-f152-47f8-b101-0610f6ea4a20 -P $THINGTOKEN -t c  hannels/e923ab60-90c7-4df9-9091-4f1c726dee84/messages
                                                (id у things 1)                 (id у channels)
Запуск mqtt_pub

1. export THINGTOKEN=14c500ec-b657-4c36-8d08-cc00d01e61e4 ("key" у things 2)

2. mosquitto_pub -u f91806e4-fecd-408e-bd79-dd8f04a73579 -P $THINGTOKEN -t channels/e923ab60-90c7-4df9-9091-4f1c726dee84/messages -m "test"
                                                (id у things 1)                 (id у channels)
