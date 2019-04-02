FROM ubuntu:16.04

RUN apt-get update && apt-get install -y build-essential xorg libssl-dev libxrender-dev wget python3 python3-pip
RUN wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.3/wkhtmltox-0.12.3_linux-generic-amd64.tar.xz && \
    tar vxf wkhtmltox-0.12.3_linux-generic-amd64.tar.xz && \
    cp wkhtmltox/bin/wk* /usr/local/bin/

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
ADD . /csv
RUN pip3 install -e /csv


ENTRYPOINT ["csv"]