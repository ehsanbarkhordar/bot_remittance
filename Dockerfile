FROM registry.bale.ai:2443/python:3.5
WORKDIR /branch_collector
RUN pip install --upgrade pip && \
    cp /usr/share/zoneinfo/Asia/Tehran /etc/localtime && \
    echo $TZ > /etc/timezone

COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt
COPY ./ /branch_collector




