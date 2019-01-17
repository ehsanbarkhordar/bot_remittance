FROM registry.bale.ai:2443/python:3.5
WORKDIR /remmitance_bot
RUN pip install --upgrade pip && \
    cp /usr/share/zoneinfo/Asia/Tehran /etc/localtime && \
    echo $TZ > /etc/timezone

COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt
COPY ./ /remmitance_bot




