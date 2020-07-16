
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

  8 ./mainflux-cli channels create '{"name":"myChannel"}' $USERTOKEN

  9 ./mainflux-cli channels get all $USERTOKEN

  10 ./mainflux-cli things connect f4d497a5-f152-47f8-b101-0610f6ea4a20 e923ab60-90c7-4df9-9091-4f1c726dee84 $USERTOKEN

