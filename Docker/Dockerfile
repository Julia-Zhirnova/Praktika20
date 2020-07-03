FROM python:3.7

MAINTAINER Julia Zhirnova <ushka666@bk.ru>

# for zero interaction while installing or upgrading the system via apt
ENV DEBIAN_FRONTEND noninteractive 

# задаем рабочую директорию для контейнера 
WORKDIR /usr/src/app

# скачиваем питон, библеотеку дл построения графиков и работы с базой данных 
RUN apt-get update && apt-get install -y python3-pip && pip3 install matplotlib influxdb \
    && apt-get install -y python3-tk 

# копируем все файлы из корня проекта в рабочую директорию
COPY programa/ /usr/src/app/programa 

# Сценарий start.sh содержит программу graphics.py & imitator.py
COPY start.sh /usr/src/app
RUN chmod -x start.sh
