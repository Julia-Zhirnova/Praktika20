FROM python:3.8

MAINTAINER Julia Zhirnova <ushka666@bk.ru>

# for zero interaction while installing or upgrading the system via apt
ENV DEBIAN_FRONTEND noninteractive

# задаем рабочую директорию для контейнера 
WORKDIR /usr/src/app

# скачиваем питон, библеотеку для построения графиков, работы с базой данных и mqtt 
RUN apt-get update && apt-get install -y python3-pip && pip3 install matplotlib influxdb flask paho-mqtt \
    && apt-get install -y python3-tk 

# копируем все файлы из корня проекта в рабочую директорию
COPY prog/ /usr/src/app/prog

# запускаем
CMD ["python3", "-m", "prog"]
