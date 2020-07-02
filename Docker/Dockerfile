FROM python:3.5

MAINTAINER Julia Zhirnova <ushka666@bk.ru>

# for zero interaction while installing or upgrading the system via apt
ENV DEBIAN_FRONTEND oninteractive 

# задаем рабочую директорию для контейнера 
WORKDIR /ust/src/app

# устанавливаем параметры сборки python
RUN apt-get update && apt-get install -y python3-pip 
# проверяем окружение python,  
RUN python3 --version
RUN pip3 --version

RUN sudo apt install virtualenv && virtualenv --python=/usr/bin/python3 && venv source venv/bin/activate # виртуальная среда питон
RUN pip install matplotlib && pip install influxdb # подключение библиотеки для построения графиков и работы с базой данных
RUN sudo apt-get install python3-tk # для построение графиков

# копируем все файлы из корня проекта в рабочую директорию
COPY programa/ /usr/src/app/programa 

# Сценарий start.sh содержит программу graphics.py & imitator.py
COPY start.sh /usr/src/app 
RUN chmod -x start.sh

# запускаем приложение  
CMD [*./start.sh*]
