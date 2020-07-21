FROM python:3.8
ENV DEBIAN_FRONTEND noninteractive
WORKDIR /usr/src/app
RUN apt-get update && apt-get install -y python3-pip && pip3 install matplotlib influxdb flask paho-mqtt pyjwt\
    && apt-get install -y python3-tk 
COPY . /usr/src/app/
CMD ["python3", "-m", "prog"]
